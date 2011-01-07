#!/usr/bin/env python
# -*- coding: utf-8 -
#chamrufzeichen
#Deutsche Rufzeichen abfragen bei der Bundesnetzagentur http://ans.bundesnetzagentur.de/
#Copyright (C) 2010 von DO1KID 

#This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#You should have received a copy of the GNU General Public License along with this program; if not, see <http://www.gnu.org/licenses/>.

from mechanize import Browser
import sys      # exit code
def main(argv=None):
	if len(argv)<=1:
		print "Kein Rufzeichen eingegeben!"
		sys.exit(1)
	if argv[1].find("*") !=-1:
		print "Kein Jokerzeichen erlaubt!"
		sys.exit(1)
	br = Browser()
	br.open("http://ans.bundesnetzagentur.de/Amateurfunk/Rufzeichen.aspx")
	br.select_form('Form1')
	br["Text1"]=argv[1];
	response=br.submit().read()
	if response.find("Kein Rufzeichen zu Ihrer Abfrage gefunden!")!= -1:
		print "Kein Rufzeichen zu Ihrer Abfrage gefunden!"
		sys.exit(1)
	begin=response.rfind(argv[1])
	if begin==-1:
		print "Rufzeichen im Quelltext nicht gefunden"
		sys.exit(1)
	end=response.find("</tr>", begin)
	if end ==-1:
		print "Ende der Tabelle konnte nicht gefunden werden"
		sys.exit(1)
	table=response[begin:end]
	table=table.replace("</font></td><td><font size=\"2\">","!")
	table=table.replace("</font></td>", "")
	while True:
		a=table.replace("  ", " ")
		if a==table:
			break
		table=a
	enum=['Rufzeichen','Klasse','persönliches Rufzeichen','Inhaber','Betriebsort']
	table=table.split("!")
	for i in range(0,len(enum)):
		print enum[i]+": " +table[i]
	sys.exit(0)

if __name__ == "__main__":
	main(sys.argv)
