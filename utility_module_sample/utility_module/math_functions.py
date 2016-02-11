# -*- encoding: utf-8 -*-
####################################################################################
#    Utility Module Sample
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


def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n is not integral or is negative")
    return n == 0 and 1 or n * factorial(n - 1)


def fibonacci(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n is not integral or is negative")
    return 0 if n == 0 else 1 if n == 1 else fibonacci(n-1) + fibonacci(n-2)
