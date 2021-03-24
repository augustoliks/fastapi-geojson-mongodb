class DomainBaseException(RuntimeError):
    pass


class AddressNotInCoverageArea(DomainBaseException):
    pass


class EmployerCNPJAlreadyRegister(DomainBaseException):
    pass


class EmployerTradeNameCNPJAlreadyRegister(DomainBaseException):
    pass
