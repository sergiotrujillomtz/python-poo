# -*- encoding: utf-8 -*-
####################################################################################
#    Inheritance Sample
#    Copyright (C) 2016  Sergio Trujillo Martínez (sergiotrujillomartinez@gmail.com)
#
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
####################################################################################


class InterfaceClass(object):

    def do_something_1(self):
        raise NotImplementedError("Should have implemented this")

    def do_something_2(self):
        raise NotImplementedError("Should have implemented this")


class AbstractClass(InterfaceClass):

    def do_something_1(self):
        """
            Implementation
        """
        return 1

    def do_something_2(self):
        """
            Implementation
        """
        return 2

    def do_something_3(self):
        raise NotImplementedError("Should have implemented this")


class ConcreteClass(AbstractClass):

    def do_something_3(self):
        """
            Implementation
        """
        return 3
