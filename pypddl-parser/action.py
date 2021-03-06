# This file is part of pypddl-parser.

# pypddl-parser is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# pypddl-parser is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with pypddl-parser.  If not, see <http://www.gnu.org/licenses/>.


class Action(object):

    def __init__(self, name, params, precond, effects):
        """

        :param name: name of the operator (e.g., 'pick-up')
        :param params:  list of Term objects (e.g., '?x' of type 'blocks')
        :param precond:
        :param effects:
        """
        self._name    = name
        self._params  = params
        self._precond = precond
        self._effects = effects

    @property
    def name(self):
        return self._name

    @property
    def params(self):
        return self._params[:]

    @property
    def precond(self):
        return self._precond[:]

    @property
    def effects(self):
        return self._effects[:]

    def __str__(self):
        operator_str  = '{0}({1})\n'.format(self._name, ', '.join(map(str, self._params)))
        operator_str += '>> precond: {0}\n'.format(', '.join(map(str, self._precond)))
        operator_str += '>> effects: {0}\n'.format(', '.join(map(str, self._effects)))
        return operator_str

    def __repr__(self):
        operator_str  = '\t(:action {name} \n' \
                        '\t\t:parameters ({param})\n' \
                        '\t\t:precondition (and {prec})\n' \
                        '\t\t:effect (and {effect})\n' \
                        '\t)'.\
            format(name = self._name,
                   param = ' '.join(repr(p) for p in self._params),
                   prec = ' '.join(repr(p) for p in self._precond),
                   effect = ' '.join(repr(e[1]) for e in self._effects)
                   )
        return operator_str
