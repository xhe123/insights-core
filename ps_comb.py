from insights import add_filter, combiner, rule, make_pass
from insights.specs import Specs

from insights.parsers.ps import PsAlxwww, PsAuxcww


# no changes required to test framework
add_filter(Specs.ps, "Network")


class Process(object):
    pass


@combiner([PsAlxwww, PsAuxcww])
class CombinedPs(object):
    def __init__(self, *args):
        self.data = args


@rule(CombinedPs)
def report(ps):
    a, b = ps.data
    return make_pass("FOO", a=a.services[:10], b=b.services[:10])
