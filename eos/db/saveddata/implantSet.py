#===============================================================================
# Copyright (C) 2016 Ryan Holmes
#
# This file is part of eos.
#
# eos is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# eos is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with eos.  If not, see <http://www.gnu.org/licenses/>.
#===============================================================================

from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relation, mapper

from eos.db import saveddata_meta
from eos.db.saveddata.implant import implantsSetMap_table
from eos.types import Implant, ImplantSet
from eos.effectHandlerHelpers import HandledImplantBoosterList

implant_set_table = Table("implantSets", saveddata_meta,
                         Column("ID", Integer, primary_key = True),
                         Column("name", String, nullable = False),
)

mapper(ImplantSet, implant_set_table,
        properties = {
            "_ImplantSet__implants": relation(
                Implant,
                collection_class = HandledImplantBoosterList,
                cascade='all, delete, delete-orphan',
                backref='set',
                single_parent=True,
                primaryjoin = implantsSetMap_table.c.setID == implant_set_table.c.ID,
                secondaryjoin = implantsSetMap_table.c.implantID == Implant.ID,
                secondary = implantsSetMap_table),
        }
)
