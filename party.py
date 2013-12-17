#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from dateutil.relativedelta import relativedelta
from datetime import datetime
from trytond.model import ModelView, ModelSingleton, ModelSQL, fields
from trytond.wizard import Wizard, StateAction, StateView, Button
from trytond.transaction import Transaction
#from trytond.backend import TableHandler
from trytond.pyson import Eval, Not, Bool, PYSONEncoder, Equal
from trytond.pool import Pool

from dateutil.relativedelta import relativedelta
from datetime import datetime
from trytond.model import ModelView, ModelSingleton, ModelSQL, fields
from trytond.wizard import Wizard, StateAction, StateView, Button
from trytond.transaction import Transaction
#from trytond.backend import TableHandler
from trytond.pyson import Eval, Not, Bool, PYSONEncoder, Equal
from trytond.pool import Pool

class Party(ModelSQL, ModelView):
    'Party'
    __name__ = 'party.party'
    
    subscription_ids = fields.One2Many('training.subscription.line', 'contact_id', 'Subscription Lines')