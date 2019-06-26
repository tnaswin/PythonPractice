#! /usr/bin/python

import sys
import datetime
import logging

import txdbinterface as txdb

from starpy import manager
from twisted.internet import reactor

extension = 0   # Takes the dialed extension
cdr = 0         # Stores the Call Details Record
ami = None      # Stores the AMIProtocol
start = 0       # Get the call start time
uid1 = 0
uid2 = 0


class OnCall():

    def __init__(self):
        self.context = None
        self.exten = None
        self.priority = None
        self.timeout = None
        self.start = None
        self.answer = None
        self.end = None
        self.duration = None
        self.disposition = "NOT ANSWERED"
        self.uniqueid = None

    def main(self):
        """Asterisk Manager Interface Login"""
        print("Main")
        f = manager.AMIFactory('aswin', '12345678')
        df = f.login(ip='192.168.5.86')
        df.addCallbacks(self.on_login, self.on_failure)
        return df

    def on_login(self, protocol):
        """On Login, attempt to originate the call"""
        global ami
        ami = protocol
        print("On Login")
        self.channel='sip/' + extension
        self.context, self.exten = 'phones', '1111'
        self.priority, self.timeout = '1', 5
        ami.events(eventmask = 'on')
        ami.registerEvent('BridgeCreate', self.on_bridge)
        ami.registerEvent('Hangup', self.on_channel_hangup)
        df = ami.originate(self.channel, self.context,
                                self.exten, self.priority, self.timeout)
        df.addCallback(self.on_finished)
        df.addErrback(self.on_failure)
        return df

    def on_finished(self, result):
        print("On Finish")
        print(result)
        global start
        start = datetime.datetime.now()
        self.start = start.strftime('%H:%M:%S')
        print start
        df = ami.status()
        return df.addCallbacks(self.on_status, self.on_failure)

    def on_status(self, details):
        "Get the Call Details Record"
        global cdr
        cdr = details
        print("On Status")
        print(cdr)

    def on_bridge(self, *args):
        """On Bridge Create event get timestamp"""
        print("Bridge")
        self.disposition = "ANSWERED"
        print(args)
        self.answer = datetime.datetime.now()
        self.answer = self.answer.strftime('%H:%M:%S')
        print answer

    def on_channel_hangup(self, ami, event):
        """Hangup of an event"""
        if event['uniqueid'] in [d['uniqueid'] for d in cdr if 'uniqueid' in d]:
            global uid1
            uid1 = event['uniqueid']
            global uid2
            uid2 = event['linkedid']
            print("Channel Hangup")
            print event
            self.uniqueid = event['uniqueid']
            print("uniqueid", event['uniqueid'])
            self.end = datetime.datetime.now()
            self.end = self.end.strftime('%H:%M:%S')
            fmt = '%H:%M:%S'
            self.duration = (datetime.datetime.strptime(self.end, fmt)
                            - datetime.datetime.strptime(self.start, fmt))
            self.insert_into_db()
            reactor.callLater(2, df.callback, event)
            ami.deregisterEvent('Hangup', on_channel_hangup)

    def insert_into_db(self):
        query = """insert into cdrdb values(calldate, dst, dcontext, channel,
                   dstchannel, lastapp, duration, disposition, uniqueid)
                   values (%s, %s, %s, %s, %s, %s, %s, %s, %s)""" %(
                   start, self.exten, self.context, cdr[1].get('channel'),
                   cdr[2].get('channel'),cdr[1].get('applications'),
                   self.duration, self.disposition, self.uniqueid)
        print query
        df = txdb.execute(query, val)
        df.addCallback(onDb)
        df.addErrback(errDb)

    def on_db(self, result):
        print("result insert db")
        print(result)
        if not result:
            return errDb(None)

    def err_db(self, error):
        print('error db')
        print(error)

    def on_failure(self, reason):
        """Unable to log in!"""
        print(reason.getTraceback())
        #hangup()


def call(ext):
    global extension
    extension = ext
    #manager.log.setLevel(logging.DEBUG)
    #logging.basicConfig()
    c = OnCall()
    reactor.callWhenRunning(c.main)
