import falcon

from example.db.manager import DBManager
from example.middleware.context import ContextMiddleware
from example.resources import scores


class MyService(falcon.API):
    def __init__(self, cfg):
        super(MyService, self).__init__(
            middleware=[ContextMiddleware()]
        )

        self.cfg = cfg

        # Build an object to manager our db connections.
        mgr = DBManager(self.cfg.db.connection)
        mgr.setup()

        # Create our resources
        scores_res = scores.ScoresResource(mgr)

        # Build routes
        self.add_route('/scores', scores_res)

    def start(self):
        """ A hook to when a Gunicorn worker calls run()."""
        pass

    def stop(self, signal):
        """ A hook to when a Gunicorn worker starts shutting down. """
        pass
