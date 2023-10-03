from dataclasses import dataclass


@dataclass
class ProcessInstance:
    bpmn_process_id: str  # the BPMN process ID of the process definition which was used to create the process instance
    process_definition_key: int  # the key of the process definition which was used to create the process instance
    process_instance_key: int  # the unique identifier of the created process instance
    version: int  # the version of the process definition which was used to create the process instance
