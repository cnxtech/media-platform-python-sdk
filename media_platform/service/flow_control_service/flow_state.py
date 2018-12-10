from media_platform.lang.serialization import Deserializable
from media_platform.service.flow_control_service.flow_error import FlowError
from media_platform.service.flow_control_service.invocation import Invocation
from media_platform.service.flow_control_service.operation import Operation


class FlowStatus(object):
    idle = 'idle'
    working = 'working'
    success = 'success'
    error = 'error'
    aborted = 'aborted'


class FlowState(Deserializable):
    def __init__(self, state_id, status, invocation, operations, flow_error=None):
        # type: (str, FlowStatus, Invocation, [str, Operation], FlowError) -> None
        super(FlowState, self).__init__()
        self.id = state_id
        self.invocation = invocation
        self.operations = operations
        self.status = status
        self.flow_error = flow_error

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> FlowState

        invocation = Invocation.deserialize(data['invocation'])
        operations_data = data.get('operations', {})
        operations = {k: Operation.deserialize(v) for k, v in operations_data.items()}
        flow_error_data = data.get('error')
        flow_error = FlowError.deserialize(flow_error_data) if flow_error_data else None

        return FlowState(data['id'], data['status'], invocation, operations, flow_error)
