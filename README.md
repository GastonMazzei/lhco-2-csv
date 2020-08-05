# lhco-2-csv
<p>An <strong>.LHCO to .csv converter</strong>.</p>
<p><em><span style="text-decoration: underline;">"Use cases include wanting HEP simulation-data transformed into a Pandas.DataFrame object"</span></em></p>
<p><span style="color: #ff0000;">To convert simply </span></p>
<p><span style="color: #ff0000;"><strong>1)</strong> run "<em>python lhco2csv.py</em>" </span></p>
<p><span style="color: #ff0000;"><strong>2)</strong> Input the name of the .LHCO file as requested by command-line-input</span></p>
<p>&nbsp;</p>
<p><span style="color: #000000;">Format INFO:</span></p>
<ul>
<li><span style="color: #000000;">Columns will be set to N times the LHCO-format columns, with N the max amount of different </span></li>
<li><span style="color: #000000;">'particles' ever observed in a collission within the file</span><br /><span style="color: #000000;">Whenever a collision has less than 'N' particles the remaining columns will be set to zero</span></li>
</ul>
<p><span style="color: #000000;">extra:<br /><em>An <span style="text-decoration: underline;">LHE-to-LHCO-converter</span> is also supplied courtesy of Mattelaer Olivier (CP3) and Rogier Van der geer</em></span></p>
