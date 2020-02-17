import logging

from alerta.plugins import PluginBase

LOG = logging.getLogger('alerta.plugins')


class Forwarder(PluginBase):
    """

    """

    def pre_receive(self, alert, **kwargs):
        return alert

    def post_receive(self, alert, **kwargs):
        # forward alert to other servers (last write wins)
        return

    def status_change(self, alert, status, text, **kwargs):
        # forward status changes to other servers
        return

    def take_action(self, alert, action, text, **kwargs):
        # trigger action on other servers
        pass

    def delete(self, alert, **kwargs) -> bool:
        # trigger delete on other servers
        pass
