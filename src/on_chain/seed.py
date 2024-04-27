from opshin.prelude import *
from opshin.ledger.interval import *


@dataclass
class ContractParams(PlutusData):

    initiator: PubKeyHash
    rngfid: bytes
    rnlen: int



@dataclass
class RefundRedeemer(PlutusData):
    pass




def validator(
    datum: ContractParams, redeemer: RefundRedeemer, context: ScriptContext
) -> None:
    assert datum.initiator in context.tx_info.signatories, "Initiator signature missing"