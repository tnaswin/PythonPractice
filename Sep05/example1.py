class Placeholder:
    """A value you don't yet have."""
    UNFIRED = object()
    def __init__(self):
        self._callbacks = []
        self._result = self.UNFIRED

    def already_fired(self):
        return not self._result is self.UNFIRED

    def when_ready(self, callable, *args, **kwargs):
        self._callbacks.append((callable, args, kwargs))
        if self.already_fired():
            self._run_callbacks()
        return self

    def _run_callbacks(self):
        while self._callbacks:
            callable, args, kwargs = self._callbacks.pop()
            self._result = callable(self._result, *args, **kwargs)

    def fire(self, value):
        if self.already_fired():
            raise AlreadyFiredError(self, value)
        self._result = value
        self._run_callbacks()
