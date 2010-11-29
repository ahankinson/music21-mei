
import music21
import doctest, unittest

mazurka = """
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<mei meiversion="2010-05" xml:id="_20090211165220956" xmlns="http://www.music-encoding.org/ns/mei">
  <meihead>
    <filedesc>
      <titlestmt>
        <title/>
      </titlestmt>
      <pubstmt/>
    </filedesc>
    <encodingdesc>
      <projectdesc>
        <p>Transcoded from a MusicXML version 1.0 file on
            <date>2009-02-11</date> using an XSLT stylesheet (2mei v.
          2.0).</p>
        <p>The MusicXML file was generated using SharpEye Music Reader
          2.</p>
      </projectdesc>
    </encodingdesc>
    <profiledesc>
      <langusage>
        <language xml:id="it"/>
      </langusage>
    </profiledesc>
  </meihead>
  <music>
    <body>
      <mdiv>
        <score>
          <scoredef meter.count="3" meter.unit="4" key.sig="0">
            <staffgrp xml:id="P1" symbol="brace" label.full="Part_1">
              <staffdef n="1" lines="5" clef.line="2" clef.shape="G"
                ppq="4" key.sig="0"/>
              <staffdef n="2" lines="5" clef.line="4" clef.shape="F"
                ppq="4" key.sig="0"/>
            </staffgrp>
          </scoredef>
          <section>
            <scoredef meter.count="3" meter.unit="4" key.sig="0"/>
            <measure n="1" xml:id="d1e12">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e47" pname="e" oct="4" dur="16"
                      dur.ges="1" stem.dir="up"/>
                    <note xml:id="d1e68" pname="a" oct="4" dur="8"
                      dots="1" dur.ges="3" stem.dir="up"/>
                    <note xml:id="d1e88" pname="c" oct="5" dur="16"
                      dur.ges="1" stem.dir="up"/>
                  </beam>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <rest xml:id="d1e112" dur="16" dur.ges="1"/>
                  <rest xml:id="d1e123" dur="4" dur.ges="4"/>
                </layer>
              </staff>
              <dynam tstamp="1" place="below" staff="1">p</dynam>
            </measure>
            <measure n="2" xml:id="d1e134">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e136" pname="e" oct="5" dur="8"
                      dots="1" dur.ges="3" stem.dir="down"/>
                    <note xml:id="d1e156" pname="e" oct="5" dur="16"
                      dur.ges="1" stem.dir="down"/>
                  </beam>
                  <note xml:id="d1e178" pname="c" oct="5" dur="4"
                    dur.ges="4" stem.dir="down"/>
                  <note xml:id="d1e196" pname="d" accid="s" oct="5"
                    dur="4" artic="acc" dur.ges="4" stem.dir="down"
                    accid.ges="s"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e224" pname="a" oct="1" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d24e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e241" pname="c" oct="4"/>
                    <note xml:id="d1e258" pname="e" oct="3"/>
                  </chord>
                  <chord xml:id="d30e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e276" pname="b" oct="3"
                      artic="acc"/>
                    <note xml:id="d1e295" pname="e" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <slur tstamp="1.75" dur="0m+2" curvedir="above"
                startid="d1e156" endid="d1e178" staff="1"/>
              <trill tstamp="3" place="above" staff="1"
                startid="d1e196"/>
            </measure>
            <measure n="3" xml:id="d1e313">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e315" pname="e" oct="5" dur="8"
                      dots="1" dur.ges="3" stem.dir="down"/>
                    <note xml:id="d1e336" pname="e" oct="5" dur="16"
                      dur.ges="1" stem.dir="down"/>
                  </beam>
                  <note xml:id="d1e357" pname="a" oct="4" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <note xml:id="d1e374" pname="c" oct="5" dur="4"
                    dur.ges="4" stem.dir="down"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e395" pname="a" oct="2" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d51e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e412" pname="c" oct="4"/>
                    <note xml:id="d1e429" pname="e" oct="3"/>
                  </chord>
                  <chord xml:id="d57e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e447" pname="c" oct="4"/>
                    <note xml:id="d1e464" pname="e" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <slur tstamp="1" dur="0m+3" curvedir="above"
                startid="d1e315" endid="d1e374" staff="1"/>
            </measure>
            <measure n="4" xml:id="d1e482">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e484" pname="b" oct="4" dur="8"
                      dots="1" dur.ges="3" stem.dir="down"/>
                    <note xml:id="d1e504" pname="b" oct="4" dur="16"
                      dur.ges="1" stem.dir="down"/>
                  </beam>
                  <note xml:id="d1e525" pname="f" accid="s" oct="4"
                    dur="4" dur.ges="4" stem.dir="up" accid.ges="s"/>
                  <note xml:id="d1e546" pname="g" accid="s" oct="4"
                    dur="4" dur.ges="4" stem.dir="up" accid.ges="s"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e572" pname="a" oct="2" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d78e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e589" pname="d" oct="4"/>
                    <note xml:id="d1e606" pname="e" oct="3"/>
                  </chord>
                  <chord xml:id="d84e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e624" pname="d" oct="4"/>
                    <note xml:id="d1e641" pname="e" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <trill tstamp="3" place="above" staff="1"
                startid="d1e546"/>
            </measure>
            <measure n="5" xml:id="d1e659">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e661" pname="a" oct="4" dur="8"
                      artic="stacciss" dur.ges="2" stem.dir="up"/>
                    <rest xml:id="d1e682" dur="16" dur.ges="1"/>
                    <note xml:id="d1e698" pname="e" oct="4" dur="16"
                      dur.ges="1" stem.dir="up"/>
                    <note xml:id="d1e720" pname="a" oct="4" dur="8"
                      artic="stacciss" dur.ges="2" stem.dir="up"/>
                    <rest xml:id="d1e742" dur="16" dur.ges="1"/>
                    <note xml:id="d1e753" pname="e" oct="4" dur="16"
                      dur.ges="1" stem.dir="up"/>
                    <note xml:id="d1e775" pname="a" oct="4" dur="8"
                      artic="stacciss" dur.ges="2" stem.dir="up"/>
                    <rest xml:id="d1e797" dur="16" dur.ges="1"/>
                    <note xml:id="d1e813" pname="c" oct="5" dur="16"
                      dur.ges="1" stem.dir="up"/>
                  </beam>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e838" pname="a" oct="2" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d105e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e855" pname="c" oct="4"/>
                    <note xml:id="d1e872" pname="e" oct="3"/>
                  </chord>
                  <chord xml:id="d111e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e890" pname="c" oct="4"/>
                    <note xml:id="d1e907" pname="e" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <hairpin tstamp="1.75" dur="0m+3.75" form="cres"
                place="below" staff="1"/>
              <slur tstamp="1.75" dur="0m+2" curvedir="below"
                startid="d1e698" endid="d1e720" staff="1"/>
              <slur tstamp="2.75" dur="0m+3" curvedir="below"
                startid="d1e753" endid="d1e775" staff="1"/>
            </measure>
            <sb/>
            <measure n="6" xml:id="d1e925">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e928" pname="e" oct="5" dur="8"
                      artic="stacciss" dur.ges="2" stem.dir="down"/>
                    <rest xml:id="d1e949" dur="16" dur.ges="1"/>
                    <note xml:id="d1e960" pname="e" oct="5" dur="16"
                      dur.ges="1" stem.dir="down"/>
                  </beam>
                  <note xml:id="d1e982" pname="c" oct="5" dur="4"
                    dur.ges="4" stem.dir="down"/>
                  <note xml:id="d1e1000" pname="d" accid="s" oct="5"
                    dur="4" artic="acc" dur.ges="4" stem.dir="down"
                    accid.ges="s"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e1028" pname="a" oct="2" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d135e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e1045" pname="c" oct="4"/>
                    <note xml:id="d1e1062" pname="e" oct="3"/>
                  </chord>
                  <chord xml:id="d141e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e1080" pname="b" oct="3"
                      artic="acc"/>
                    <note xml:id="d1e1100" pname="e" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <slur tstamp="1.75" dur="0m+2" curvedir="above"
                startid="d1e960" endid="d1e982" staff="1"/>
              <trill tstamp="3" place="above" staff="1"
                startid="d1e1000"/>
            </measure>
            <measure n="7" xml:id="d1e1118">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e1120" pname="e" oct="5" dur="8"
                      dots="1" dur.ges="3" stem.dir="down"/>
                    <note xml:id="d1e1141" pname="e" oct="5" dur="16"
                      dur.ges="1" stem.dir="down"/>
                  </beam>
                  <note xml:id="d1e1162" pname="a" oct="4" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <note xml:id="d1e1179" pname="c" oct="5" dur="4"
                    dur.ges="4" stem.dir="down"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e1200" pname="a" oct="2" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d162e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e1217" pname="c" oct="4"/>
                    <note xml:id="d1e1234" pname="e" oct="3"/>
                  </chord>
                  <chord xml:id="d168e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e1252" pname="c" oct="4"/>
                    <note xml:id="d1e1269" pname="e" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <slur tstamp="1" dur="0m+3" curvedir="above"
                startid="d1e1120" endid="d1e1179" staff="1"/>
            </measure>
            <measure n="8" xml:id="d1e1287">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e1289" pname="b" oct="4" dur="8"
                      dots="1" dur.ges="3" stem.dir="down"/>
                    <note xml:id="d1e1309" pname="b" oct="4" dur="16"
                      dur.ges="1" stem.dir="down"/>
                  </beam>
                  <note xml:id="d1e1330" pname="f" accid="s" oct="4"
                    dur="4" dur.ges="4" stem.dir="up" accid.ges="s"/>
                  <note xml:id="d1e1351" pname="g" accid="s" oct="4"
                    dur="4" dur.ges="4" stem.dir="up" accid.ges="s"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e1377" pname="a" oct="2" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d189e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e1394" pname="d" oct="4"/>
                    <note xml:id="d1e1411" pname="e" oct="3"/>
                  </chord>
                  <chord xml:id="d195e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e1429" pname="d" oct="4"/>
                    <note xml:id="d1e1446" pname="e" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <trill tstamp="3" place="above" staff="1"
                startid="d1e1351"/>
            </measure>
            <measure n="9" xml:id="d1e1464">
              <staff n="1">
                <layer n="1">
                  <note xml:id="d1e1466" pname="a" oct="5" dur="4"
                    dur.ges="4" stem.dir="down"/>
                  <rest xml:id="d1e1483" dur="8" dots="1" dur.ges="3"/>
                  <beam>
                    <note xml:id="d1e1495" pname="e" oct="4" dur="16"
                      dur.ges="1" stem.dir="up"/>
                    <note xml:id="d1e1517" pname="a" oct="4" dur="8"
                      dots="1" dur.ges="3" stem.dir="up"/>
                    <note xml:id="d1e1537" pname="c" oct="5" dur="16"
                      dur.ges="1" stem.dir="up"/>
                  </beam>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e1561" pname="a" oct="2" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d214e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e1578" pname="c" oct="4"/>
                    <note xml:id="d1e1595" pname="e" oct="3"/>
                  </chord>
                  <rest xml:id="d1e1613" dur="4" dur.ges="4"/>
                </layer>
              </staff>
              <slur tstamp="2.75" dur="1m+1" curvedir="below"
                startid="d1e1495" endid="d1e1627" staff="1"/>
            </measure>
            <measure n="10" xml:id="d1e1625">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e1627" pname="e" oct="5" dur="8"
                      dots="1" dur.ges="3" stem.dir="down"/>
                    <note xml:id="d1e1648" pname="e" oct="5" dur="16"
                      dur.ges="1" stem.dir="down"/>
                  </beam>
                  <note xml:id="d1e1669" pname="c" oct="5" dur="4"
                    dur.ges="4" stem.dir="down"/>
                  <note xml:id="d1e1686" pname="d" accid="s" oct="5"
                    dur="4" dur.ges="4" stem.dir="down" accid.ges="s"
                  />
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e1712" pname="a" oct="1" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d235e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e1729" pname="c" oct="4"/>
                    <note xml:id="d1e1746" pname="e" oct="3"/>
                  </chord>
                  <chord xml:id="d241e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e1764" pname="b" oct="3"
                      artic="acc"/>
                    <note xml:id="d1e1783" pname="e" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <trill tstamp="3" place="above" staff="1"
                startid="d1e1686"/>
            </measure>
            <measure n="11" xml:id="d1e1801">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e1803" pname="e" oct="5" dur="8"
                      dots="1" dur.ges="3" stem.dir="down"/>
                    <note xml:id="d1e1824" pname="e" oct="5" dur="16"
                      dur.ges="1" stem.dir="down"/>
                  </beam>
                  <note xml:id="d1e1845" pname="a" oct="4" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <note xml:id="d1e1862" pname="c" oct="5" dur="4"
                    dur.ges="4" stem.dir="down"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e1883" pname="a" oct="2" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d260e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e1900" pname="c" oct="4"/>
                    <note xml:id="d1e1917" pname="e" oct="3"/>
                  </chord>
                  <chord xml:id="d266e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e1935" pname="c" oct="4"/>
                    <note xml:id="d1e1952" pname="e" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <slur tstamp="1" dur="0m+3" curvedir="above"
                startid="d1e1803" endid="d1e1862" staff="1"/>
            </measure>
            <sb/>
            <measure n="12" xml:id="d1e1970">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e1973" pname="b" oct="4" dur="8"
                      dots="1" dur.ges="3" stem.dir="down"/>
                    <note xml:id="d1e1993" pname="b" oct="4" dur="16"
                      dur.ges="1" stem.dir="down"/>
                  </beam>
                  <note xml:id="d1e2014" pname="f" accid="s" oct="4"
                    dur="4" dur.ges="4" stem.dir="up" accid.ges="s"/>
                  <note xml:id="d1e2035" pname="g" accid="s" oct="4"
                    dur="4" dur.ges="4" stem.dir="up" accid.ges="s"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e2061" pname="a" oct="2" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d287e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e2078" pname="d" oct="4"/>
                    <note xml:id="d1e2095" pname="e" oct="3"/>
                  </chord>
                  <chord xml:id="d293e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e2113" pname="d" oct="4"/>
                    <note xml:id="d1e2130" pname="e" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <trill tstamp="3" place="above" staff="1"
                startid="d1e2035"/>
            </measure>
            <measure n="13" xml:id="d1e2148">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e2150" pname="a" oct="4" dur="8"
                      artic="stacciss" dur.ges="2" stem.dir="up"/>
                    <rest xml:id="d1e2171" dur="16" dur.ges="1"/>
                    <note xml:id="d1e2187" pname="e" oct="4" dur="16"
                      dur.ges="1" stem.dir="up"/>
                    <note xml:id="d1e2209" pname="a" oct="4" dur="8"
                      artic="stacciss" dur.ges="2" stem.dir="up"/>
                    <rest xml:id="d1e2231" dur="16" dur.ges="1"/>
                    <note xml:id="d1e2242" pname="e" oct="4" dur="16"
                      dur.ges="1" stem.dir="up"/>
                    <note xml:id="d1e2264" pname="a" oct="4" dur="8"
                      artic="stacciss" dur.ges="2" stem.dir="up"/>
                    <rest xml:id="d1e2286" dur="16" dur.ges="1"/>
                    <note xml:id="d1e2302" pname="c" oct="5" dur="16"
                      dur.ges="1" stem.dir="up"/>
                  </beam>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e2328" pname="a" oct="2" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d314e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e2345" pname="c" oct="4"/>
                    <note xml:id="d1e2362" pname="e" oct="3"/>
                  </chord>
                  <chord xml:id="d320e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e2380" pname="c" oct="4"/>
                    <note xml:id="d1e2397" pname="e" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <hairpin tstamp="1.75" dur="0m+3.75" form="cres"
                place="below" staff="1"/>
              <slur tstamp="1.75" dur="0m+2" curvedir="below"
                startid="d1e2187" endid="d1e2209" staff="1"/>
              <slur tstamp="2.75" dur="0m+3" curvedir="below"
                startid="d1e2242" endid="d1e2264" staff="1"/>
              <slur tstamp="3.75" dur="1m+1" curvedir="below"
                startid="d1e2302" endid="d1e2417" staff="1"/>
            </measure>
            <measure n="14" xml:id="d1e2415">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e2417" pname="e" oct="5" dur="8"
                      artic="stacciss" dur.ges="2" stem.dir="down"/>
                    <rest xml:id="d1e2439" dur="16" dur.ges="1"/>
                    <note xml:id="d1e2450" pname="e" oct="5" dur="16"
                      dur.ges="1" stem.dir="down"/>
                  </beam>
                  <note xml:id="d1e2472" pname="c" oct="5" dur="4"
                    dur.ges="4" stem.dir="down"/>
                  <note xml:id="d1e2490" pname="d" accid="s" oct="5"
                    dur="4" dur.ges="4" stem.dir="down" accid.ges="s"
                  />
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e2516" pname="a" oct="2" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d348e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e2533" pname="c" oct="4"/>
                    <note xml:id="d1e2550" pname="e" oct="3"/>
                  </chord>
                  <chord xml:id="d354e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e2568" pname="b" oct="3"
                      artic="acc"/>
                    <note xml:id="d1e2587" pname="e" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <slur tstamp="1.75" dur="0m+2" curvedir="above"
                startid="d1e2450" endid="d1e2472" staff="1"/>
              <trill tstamp="3" place="above" staff="1"
                startid="d1e2490"/>
            </measure>
            <measure n="15" xml:id="d1e2605">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e2607" pname="e" oct="5" dur="8"
                      dots="1" dur.ges="3" stem.dir="down"/>
                    <note xml:id="d1e2628" pname="e" oct="5" dur="16"
                      dur.ges="1" stem.dir="down"/>
                  </beam>
                  <note xml:id="d1e2649" pname="a" oct="4" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <note xml:id="d1e2666" pname="c" oct="5" dur="4"
                    dur.ges="4" stem.dir="down"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e2687" pname="a" oct="2" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d375e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e2704" pname="c" oct="4"/>
                    <note xml:id="d1e2721" pname="e" oct="3"/>
                  </chord>
                  <chord xml:id="d381e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e2739" pname="c" oct="4"/>
                    <note xml:id="d1e2756" pname="e" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <slur tstamp="1" dur="0m+3" curvedir="above"
                startid="d1e2607" endid="d1e2666" staff="1"/>
            </measure>
            <measure n="16" xml:id="d1e2774">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e2776" pname="b" oct="4" dur="8"
                      dots="1" dur.ges="3" stem.dir="down"/>
                    <note xml:id="d1e2796" pname="b" oct="4" dur="16"
                      dur.ges="1" stem.dir="down"/>
                  </beam>
                  <note xml:id="d1e2817" pname="f" accid="s" oct="4"
                    dur="4" dur.ges="4" stem.dir="up" accid.ges="s"/>
                  <note xml:id="d1e2838" pname="g" accid="s" oct="4"
                    dur="4" dur.ges="4" stem.dir="up" accid.ges="s"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e2864" pname="a" oct="2" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d402e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e2881" pname="d" oct="4"/>
                    <note xml:id="d1e2898" pname="e" oct="3"/>
                  </chord>
                  <chord xml:id="d408e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e2916" pname="d" oct="4"/>
                    <note xml:id="d1e2933" pname="e" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <trill tstamp="3" place="above" staff="1"
                startid="d1e2838"/>
            </measure>
            <measure n="17" xml:id="d1e2951" right="rptstart">
              <staff n="1">
                <layer n="1">
                  <note xml:id="d1e2953" pname="a" oct="5" dur="4"
                    dur.ges="4" stem.dir="down"/>
                  <rest xml:id="d1e2970" dur="8" dots="1" dur.ges="3"/>
                  <beam>
                    <note xml:id="d1e2982" pname="g" accid="n" oct="4"
                      dur="16" dur.ges="1" stem.dir="down"/>
                    <note xml:id="d1e3006" pname="c" oct="5" dur="8"
                      dots="1" dur.ges="3" stem.dir="down"/>
                    <note xml:id="d1e3026" pname="e" oct="5" dur="16"
                      dur.ges="1" stem.dir="down"/>
                  </beam>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <chord xml:id="d426e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e3050" pname="c" oct="4"/>
                    <note xml:id="d1e3067" pname="a" oct="3"/>
                  </chord>
                  <rest xml:id="d1e3085" dur="4" dur.ges="4"/>
                  <rest xml:id="d1e3096" dur="4" dur.ges="4"/>
                </layer>
              </staff>
              <slur tstamp="2.75" dur="1m+1" curvedir="above"
                startid="d1e2982" endid="d1e3118" staff="1"/>
            </measure>
          </section>
          <section>
            <sb/>
            <measure n="18" xml:id="d1e3110" left="rptstart">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e3118" pname="g" oct="5" dur="8"
                      dots="1" dur.ges="3" stem.dir="down"/>
                    <note xml:id="d1e3139" pname="g" oct="5" dur="16"
                      dur.ges="1" stem.dir="down"/>
                  </beam>
                  <note xml:id="d1e3160" pname="e" oct="5" dur="4"
                    dur.ges="4" stem.dir="down"/>
                  <note xml:id="d1e3177" pname="f" accid="s" oct="5"
                    dur="4" artic="acc" dur.ges="4" stem.dir="down"
                    accid.ges="s"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e3205" pname="c" oct="3" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d447e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e3222" pname="e" oct="4"/>
                    <note xml:id="d1e3239" pname="g" oct="3"/>
                  </chord>
                  <chord xml:id="d453e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e3258" pname="d" accid="s" oct="4"
                      artic="acc" accid.ges="s"/>
                    <note xml:id="d1e3281" pname="g" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <trill tstamp="3" place="above" staff="1"
                startid="d1e3177"/>
            </measure>
            <measure n="19" xml:id="d1e3299">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e3301" pname="g" oct="5" dur="8"
                      dots="1" dur.ges="3" stem.dir="down"/>
                    <note xml:id="d1e3321" pname="g" oct="5" dur="16"
                      dur.ges="1" stem.dir="down"/>
                  </beam>
                  <note xml:id="d1e3342" pname="e" accid="n" oct="5"
                    dur="4" dur.ges="4" stem.dir="down"/>
                  <note xml:id="d1e3361" pname="f" accid="s" oct="5"
                    dur="4" artic="acc" dur.ges="4" stem.dir="down"
                    accid.ges="s"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e3389" pname="c" oct="3" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d472e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e3406" pname="e" oct="4"/>
                    <note xml:id="d1e3423" pname="g" oct="3"/>
                  </chord>
                  <chord xml:id="d478e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e3441" pname="d" accid="s" oct="4"
                      artic="acc" accid.ges="s"/>
                    <note xml:id="d1e3464" pname="g" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <trill tstamp="3" place="above" staff="1"
                startid="d1e3361"/>
            </measure>
            <measure n="20" xml:id="d1e3482">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e3484" pname="g" oct="5" dur="8"
                      dur.ges="2" stem.dir="down"/>
                    <rest vo="3" xml:id="d1e3503" dur="16" dur.ges="1"/>
                    <note xml:id="d1e3518" pname="g" oct="5" dur="16"
                      dur.ges="1" stem.dir="down"/>
                  </beam>
                  <note xml:id="d1e3540" pname="c" oct="5" dur="4"
                    dur.ges="4" stem.dir="down"/>
                  <note xml:id="d1e3558" pname="d" oct="5" dur="4"
                    artic="acc" dur.ges="4" stem.dir="down"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e3580" pname="c" oct="3" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d497e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e3597" pname="e" oct="4"/>
                    <note xml:id="d1e3614" pname="g" oct="3"/>
                  </chord>
                  <chord xml:id="d503e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e3632" pname="f" oct="4"
                      artic="acc"/>
                    <note xml:id="d1e3651" pname="g" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <slur tstamp="1.75" dur="0m+2" curvedir="above"
                startid="d1e3518" endid="d1e3540" staff="1"/>
            </measure>
            <measure n="21" xml:id="d1e3670">
              <staff n="1">
                <layer n="1">
                  <note xml:id="d1e3672" pname="e" oct="5" dur="2"
                    dots="1" dur.ges="12" stem.dir="down"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e3693" pname="c" oct="3" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d521e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e3710" pname="e" oct="4"/>
                    <note xml:id="d1e3728" pname="g" oct="3"/>
                  </chord>
                  <chord xml:id="d527e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e3746" pname="d" oct="4"/>
                    <note xml:id="d1e3764" pname="g" accid="s" oct="3"
                      accid.ges="s"/>
                    <note xml:id="d1e3786" pname="e" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <slur tstamp="2" dur="0m+3" curvedir="above"
                startid="d1e3710" endid="d1e3746" staff="2"/>
            </measure>
            <measure n="22" xml:id="d1e3804">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e3812" pname="e" oct="5" dur="8"
                      dots="1" dur.ges="3" stem.dir="down"/>
                    <note xml:id="d1e3832" pname="e" oct="5" dur="16"
                      dur.ges="1" stem.dir="down"/>
                  </beam>
                  <note xml:id="d1e3853" pname="c" oct="5" dur="4"
                    dur.ges="4" stem.dir="down"/>
                  <note xml:id="d1e3870" pname="d" accid="s" oct="5"
                    dur="4" dur.ges="4" stem.dir="down" accid.ges="s"
                  />
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e3896" pname="a" oct="1" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d549e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e3913" pname="c" oct="4"/>
                    <note xml:id="d1e3930" pname="e" oct="3"/>
                  </chord>
                  <chord xml:id="d555e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e3948" pname="b" oct="3"
                      artic="acc"/>
                    <note xml:id="d1e3967" pname="e" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <dynam tstamp="1" place="below" staff="1">p</dynam>
              <trill tstamp="3" place="above" staff="1"
                startid="d1e3870"/>
            </measure>
            <measure n="23" xml:id="d1e3985">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e3987" pname="e" oct="5" dur="8"
                      dots="1" dur.ges="3" stem.dir="down"/>
                    <note xml:id="d1e4008" pname="e" oct="5" dur="16"
                      dur.ges="1" stem.dir="down"/>
                  </beam>
                  <note xml:id="d1e4029" pname="a" oct="4" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <note xml:id="d1e4046" pname="c" oct="5" dur="4"
                    dur.ges="4" stem.dir="down"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e4067" pname="a" oct="2" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d574e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e4084" pname="c" oct="4"/>
                    <note xml:id="d1e4101" pname="e" oct="3"/>
                  </chord>
                  <chord xml:id="d580e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e4119" pname="c" oct="4"/>
                    <note xml:id="d1e4136" pname="e" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <slur tstamp="1" dur="0m+3" curvedir="above"
                startid="d1e3987" endid="d1e4046" staff="1"/>
            </measure>
            <measure n="24" xml:id="d1e4154">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e4156" pname="b" oct="4" dur="8"
                      dots="1" dur.ges="3" stem.dir="down"/>
                    <note xml:id="d1e4176" pname="b" oct="4" dur="16"
                      dur.ges="1" stem.dir="down"/>
                  </beam>
                  <note xml:id="d1e4197" pname="f" accid="s" oct="4"
                    dur="4" dur.ges="4" stem.dir="up" accid.ges="s"/>
                  <note xml:id="d1e4218" pname="g" accid="s" oct="4"
                    dur="4" dur.ges="4" stem.dir="up" accid.ges="s"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e4244" pname="a" oct="2" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d601e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e4261" pname="d" oct="4"/>
                    <note xml:id="d1e4278" pname="e" oct="3"/>
                  </chord>
                  <chord xml:id="d607e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e4296" pname="d" oct="4"/>
                    <note xml:id="d1e4313" pname="e" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <trill tstamp="3" place="above" staff="1"
                startid="d1e4218"/>
            </measure>
            <sb/>
            <measure n="25" xml:id="d1e4331">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e4339" pname="a" oct="4" dur="8"
                      dur.ges="2" stem.dir="up"/>
                    <rest xml:id="d1e4358" dur="16" dur.ges="1"/>
                    <note xml:id="d1e4369" pname="e" oct="4" dur="16"
                      dur.ges="1" stem.dir="up"/>
                    <note xml:id="d1e4391" pname="a" oct="4" dur="8"
                      artic="stacciss" dur.ges="2" stem.dir="up"/>
                    <rest xml:id="d1e4413" dur="16" dur.ges="1"/>
                    <note xml:id="d1e4424" pname="e" oct="4" dur="16"
                      dur.ges="1" stem.dir="up"/>
                    <note xml:id="d1e4446" pname="a" oct="4" dur="8"
                      artic="stacciss" dur.ges="2" stem.dir="up"/>
                    <rest xml:id="d1e4468" dur="16" dur.ges="1"/>
                    <note xml:id="d1e4485" pname="c" oct="5" dur="16"
                      dur.ges="1" stem.dir="up"/>
                  </beam>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e4510" pname="a" oct="2" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d628e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e4527" pname="c" oct="4"/>
                    <note xml:id="d1e4544" pname="e" oct="3"/>
                  </chord>
                  <chord xml:id="d634e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e4562" pname="c" oct="4"/>
                    <note xml:id="d1e4579" pname="e" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <hairpin tstamp="1" dur="0m+3.75" form="cres"
                place="below" staff="1"/>
              <slur tstamp="1.75" dur="0m+2" curvedir="below"
                startid="d1e4369" endid="d1e4391" staff="1"/>
              <slur tstamp="2.75" dur="0m+3" curvedir="below"
                startid="d1e4424" endid="d1e4446" staff="1"/>
              <slur tstamp="3.75" dur="1m+1" curvedir="below"
                startid="d1e4485" endid="d1e4599" staff="1"/>
            </measure>
            <measure n="26" xml:id="d1e4597">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e4599" pname="e" oct="5" dur="8"
                      dur.ges="2" stem.dir="down"/>
                    <rest xml:id="d1e4619" dur="16" dur.ges="1"/>
                    <note xml:id="d1e4630" pname="e" oct="5" dur="16"
                      dur.ges="1" stem.dir="down"/>
                  </beam>
                  <note xml:id="d1e4652" pname="c" oct="5" dur="4"
                    dur.ges="4" stem.dir="down"/>
                  <note xml:id="d1e4670" pname="d" accid="s" oct="5"
                    dur="4" artic="acc" dur.ges="4" stem.dir="down"
                    accid.ges="s"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e4698" pname="a" oct="2" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d662e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e4715" pname="c" oct="4"/>
                    <note xml:id="d1e4732" pname="e" oct="3"/>
                  </chord>
                  <chord xml:id="d668e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e4750" pname="b" oct="3"/>
                    <note xml:id="d1e4767" pname="e" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <slur tstamp="1.75" dur="0m+2" curvedir="above"
                startid="d1e4630" endid="d1e4652" staff="1"/>
              <trill tstamp="3" place="above" staff="1"
                startid="d1e4670"/>
            </measure>
            <measure n="27" xml:id="d1e4785">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e4787" pname="e" oct="5" dur="8"
                      dots="1" dur.ges="3" stem.dir="down"/>
                    <note xml:id="d1e4807" pname="e" oct="5" dur="16"
                      dur.ges="1" stem.dir="down"/>
                  </beam>
                  <note xml:id="d1e4828" pname="a" oct="4" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <note xml:id="d1e4845" pname="c" oct="5" dur="4"
                    dur.ges="4" stem.dir="down"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e4865" pname="a" oct="2" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d689e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e4882" pname="c" oct="4"/>
                    <note xml:id="d1e4899" pname="e" oct="3"/>
                  </chord>
                  <chord xml:id="d695e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e4917" pname="c" oct="4"/>
                    <note xml:id="d1e4934" pname="e" oct="3"/>
                  </chord>
                </layer>
              </staff>
            </measure>
            <measure n="28" xml:id="d1e4952">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e4954" pname="b" oct="4" dur="8"
                      dots="1" dur.ges="3" stem.dir="down"/>
                    <note xml:id="d1e4974" pname="b" oct="4" dur="16"
                      dur.ges="1" stem.dir="down"/>
                  </beam>
                  <note xml:id="d1e4995" pname="f" accid="s" oct="4"
                    dur="4" dur.ges="4" stem.dir="up" accid.ges="s"/>
                  <note xml:id="d1e5016" pname="g" accid="s" oct="4"
                    dur="4" dur.ges="4" stem.dir="up" accid.ges="s"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e5042" pname="a" oct="2" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d714e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e5059" pname="d" oct="4"/>
                    <note xml:id="d1e5076" pname="e" oct="3"/>
                  </chord>
                  <chord xml:id="d720e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e5094" pname="d" oct="4"/>
                    <note xml:id="d1e5111" pname="e" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <trill tstamp="3" place="above" staff="1"
                startid="d1e5016"/>
            </measure>
            <measure n="29" xml:id="d1e5129" right="rptend">
              <staff n="1">
                <layer n="1">
                  <note xml:id="d1e5131" pname="a" oct="5" dur="4"
                    dur.ges="4" stem.dir="down"/>
                  <rest xml:id="d1e5148" dur="8" dots="1" dur.ges="3"/>
                  <beam>
                    <note xml:id="d1e5160" pname="g" accid="n" oct="4"
                      dur="16" dur.ges="1" stem.dir="down"/>
                    <note xml:id="d1e5183" pname="c" oct="5" dur="8"
                      dots="1" dur.ges="3" stem.dir="down"/>
                    <note xml:id="d1e5204" pname="e" oct="5" dur="16"
                      dur.ges="1" stem.dir="down"/>
                  </beam>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e5229" pname="a" oct="2" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d739e1" dur="8" dur.ges="2"
                    stem.dir="down">
                    <note xml:id="d1e5246" pname="c" oct="4"/>
                    <note xml:id="d1e5263" pname="e" oct="3"/>
                  </chord>
                  <rest xml:id="d1e5281" dur="8" dur.ges="2"/>
                  <rest xml:id="d1e5292" dur="4" dur.ges="4"/>
                </layer>
              </staff>
              <slur tstamp="3" dur="0m+3.75" curvedir="above"
                startid="d1e5183" endid="d1e5204" staff="1"/>
            </measure>
          </section>
          <section>
            <measure n="30" xml:id="d1e5308" right="rptstart">
              <staff n="1">
                <layer n="1">
                  <note xml:id="d1e5310" pname="a" oct="5" dur="4"
                    dur.ges="4" stem.dir="down"/>
                  <rest xml:id="d1e5327" dur="8" dots="1" dur.ges="3"/>
                  <beam>
                    <note xml:id="d1e5339" pname="e" oct="4" dur="16"
                      dur.ges="1" stem.dir="up"/>
                    <note xml:id="d1e5361" pname="e" oct="4" dur="8"
                      dots="1" dur.ges="3" stem.dir="up"/>
                    <note xml:id="d1e5381" pname="e" oct="4" dur="16"
                      dur.ges="1" stem.dir="up"/>
                  </beam>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e5406" pname="a" oct="2" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d760e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e5423" pname="c" oct="4"/>
                    <note xml:id="d1e5440" pname="e" oct="3"/>
                  </chord>
                  <rest xml:id="d1e5458" dur="4" dur.ges="4"/>
                </layer>
              </staff>
              <slur tstamp="2.75" dur="0m+3.75" curvedir="below"
                startid="d1e5339" endid="d1e5381" staff="1"/>
            </measure>
          </section>
          <section>
            <sb/>
            <scoredef key.sig="3s"/>
            <measure n="31" xml:id="d1e5472" left="rptstart">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e5530" pname="c" oct="5" dur="8"
                      dots="1" dur.ges="3" stem.dir="up" accid.ges="s"/>
                    <note xml:id="d1e5557" pname="c" oct="5" dur="16"
                      dur.ges="1" stem.dir="up" accid.ges="s"/>
                  </beam>
                  <note xml:id="d1e5608" pname="e" oct="4" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <note xml:id="d1e5648" pname="a" oct="4" dur="4"
                    dur.ges="4" stem.dir="up"/>
                </layer>
                <layer n="2">
                  <chord xml:id="d776e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e5490" pname="e" oct="4"/>
                    <note xml:id="d1e5507" pname="c" oct="4"
                      accid.ges="s"/>
                  </chord>
                  <note xml:id="d1e5586" pname="c" oct="4" dur="4"
                    dur.ges="4" stem.dir="down" accid.ges="s"/>
                  <note xml:id="d1e5626" pname="c" oct="4" dur="4"
                    dur.ges="4" stem.dir="down" accid.ges="s"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <chord xml:id="d788e1" dur="4" dur.ges="4"
                    stem.dir="up">
                    <note xml:id="d1e5669" pname="e" oct="3"/>
                    <note xml:id="d1e5686" pname="a" oct="2"/>
                  </chord>
                  <chord xml:id="d794e1" dur="4" dur.ges="4"
                    stem.dir="up">
                    <note xml:id="d1e5704" pname="e" oct="3"/>
                    <note xml:id="d1e5722" pname="a" oct="2"/>
                  </chord>
                  <chord xml:id="d800e1" dur="4" dur.ges="4"
                    stem.dir="up">
                    <note xml:id="d1e5740" pname="e" oct="3"/>
                    <note xml:id="d1e5757" pname="a" oct="2"/>
                  </chord>
                </layer>
              </staff>
              <dynam tstamp="1" place="below" staff="1">mf</dynam>
              <hairpin tstamp="1.75" dur="0m+2" form="cres"
                place="below" staff="1"/>
              <slur tstamp="2" dur="0m+3" curvedir="below"
                startid="d1e5608" endid="d1e5648" staff="1"/>
            </measure>
            <measure n="32" xml:id="d1e5776">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e5818" pname="c" oct="5" dur="8"
                      dots="1" dur.ges="3" stem.dir="up" accid.ges="s"/>
                    <note xml:id="d1e5840" pname="c" oct="5" dur="16"
                      dur.ges="1" stem.dir="up" accid.ges="s"/>
                  </beam>
                  <note xml:id="d1e5885" pname="e" oct="4" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <note xml:id="d1e5925" pname="a" oct="4" dur="4"
                    dur.ges="4" stem.dir="up"/>
                </layer>
                <layer n="2">
                  <chord xml:id="d817e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e5778" pname="e" oct="4"/>
                    <note xml:id="d1e5795" pname="c" oct="4"
                      accid.ges="s"/>
                  </chord>
                  <note xml:id="d1e5863" pname="c" oct="4" dur="4"
                    dur.ges="4" stem.dir="down" accid.ges="s"/>
                  <note xml:id="d1e5903" pname="c" oct="4" dur="4"
                    dur.ges="4" stem.dir="down" accid.ges="s"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1" visible="false">
                  <beam>
                    <space xml:id="d850e9" dur.ges="3"/>
                    <space xml:id="d850e10" dur.ges="1"/>
                  </beam>
                  <space xml:id="d850e11" dur.ges="4"/>
                  <space xml:id="d850e12" dur.ges="4"/>
                </layer>
                <layer n="2">
                  <chord xml:id="d829e1" dur="4" dur.ges="4"
                    stem.dir="up">
                    <note xml:id="d1e5947" pname="e" oct="3"/>
                    <note xml:id="d1e5964" pname="a" oct="2"/>
                  </chord>
                  <chord xml:id="d835e1" dur="4" dur.ges="4"
                    stem.dir="up">
                    <note xml:id="d1e5982" pname="e" oct="3"/>
                    <note xml:id="d1e5999" pname="a" oct="2"/>
                  </chord>
                  <chord xml:id="d841e1" dur="4" dur.ges="4"
                    stem.dir="up">
                    <note xml:id="d1e6017" pname="e" oct="3"/>
                    <note xml:id="d1e6034" pname="a" oct="2"/>
                  </chord>
                </layer>
              </staff>
              <slur tstamp="2" dur="0m+3" curvedir="below"
                startid="d1e5885" endid="d1e5925" staff="1"/>
            </measure>
            <measure n="33" xml:id="d1e6060">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <chord xml:id="d857e1" dur="8" dots="1"
                      dur.ges="3" stem.dir="down">
                      <note xml:id="d1e6068" pname="e" oct="5"/>
                      <note xml:id="d1e6089" pname="c" oct="5"
                        accid.ges="s"/>
                    </chord>
                    <chord xml:id="d863e1" dur="16" dur.ges="1"
                      stem.dir="down">
                      <note xml:id="d1e6110" pname="d" accid="s"
                        oct="5" accid.ges="s"/>
                      <note xml:id="d1e6135" pname="b" accid="s"
                        oct="4" accid.ges="s"/>
                    </chord>
                  </beam>
                  <chord xml:id="d869e1" dur="4" dots="1" dur.ges="6"
                    stem.dir="down">
                    <note xml:id="d1e6157" pname="f" oct="5"
                      accid.ges="s"/>
                    <note xml:id="d1e6177" pname="d" accid="n" oct="5"
                    />
                  </chord>
                  <chord xml:id="d875e1" dur="8" dur.ges="2"
                    stem.dir="down">
                    <note xml:id="d1e6198" pname="e" oct="5"/>
                    <note xml:id="d1e6216" pname="c" oct="5"
                      accid.ges="s"/>
                  </chord>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <beam>
                    <chord xml:id="d882e1" dur="8" dots="1"
                      dur.ges="3" stem.dir="up">
                      <note xml:id="d1e6261" pname="e" oct="4"/>
                      <note xml:id="d1e6282" pname="c" oct="4"
                        accid.ges="s"/>
                    </chord>
                    <chord xml:id="d888e1" dur="16" dur.ges="1"
                      stem.dir="up">
                      <note xml:id="d1e6303" pname="d" accid="s"
                        oct="4" accid.ges="s"/>
                      <note xml:id="d1e6328" pname="b" accid="s"
                        oct="3" accid.ges="s"/>
                    </chord>
                  </beam>
                  <chord xml:id="d894e1" dur="4" dots="1" dur.ges="6"
                    stem.dir="up">
                    <note xml:id="d1e6350" pname="f" oct="4"
                      accid.ges="s"/>
                    <note xml:id="d1e6370" pname="d" accid="n" oct="4"
                    />
                  </chord>
                  <chord xml:id="d900e1" dur="8" dur.ges="2"
                    stem.dir="up">
                    <note xml:id="d1e6391" pname="e" oct="4"/>
                    <note xml:id="d1e6409" pname="c" oct="4"
                      accid.ges="s"/>
                  </chord>
                </layer>
                <layer n="2">
                  <note xml:id="d1e6239" pname="a" oct="3" dur="2"
                    dots="1" dur.ges="12" stem.dir="down"/>
                </layer>
              </staff>
              <dynam tstamp="1" place="below" staff="1">f</dynam>
              <slur tstamp="1" dur="0m+3.5" curvedir="above"
                startid="d1e6068" endid="d1e6198" staff="1"/>
              <slur tstamp="1" dur="0m+3.5" curvedir="below"
                startid="d1e6261" endid="d1e6391" staff="2"/>
            </measure>
            <measure n="34" xml:id="d1e6429">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <chord xml:id="d918e1" dur="8" dots="1"
                      dur.ges="3" stem.dir="down">
                      <note xml:id="d1e6437" pname="e" oct="5"/>
                      <note xml:id="d1e6457" pname="c" oct="5"
                        accid.ges="s"/>
                    </chord>
                    <chord xml:id="d924e1" dur="16" dur.ges="1"
                      stem.dir="down">
                      <note xml:id="d1e6478" pname="d" accid="s"
                        oct="5" accid.ges="s"/>
                      <note xml:id="d1e6503" pname="b" accid="s"
                        oct="4" accid.ges="s"/>
                    </chord>
                  </beam>
                  <chord xml:id="d930e1" dur="4" dots="1" dur.ges="6"
                    stem.dir="down">
                    <note xml:id="d1e6525" pname="f" oct="5"
                      accid.ges="s"/>
                    <note xml:id="d1e6545" pname="d" accid="n" oct="5"
                    />
                  </chord>
                  <chord xml:id="d936e1" dur="8" dur.ges="2"
                    stem.dir="down">
                    <note xml:id="d1e6566" pname="e" oct="5"/>
                    <note xml:id="d1e6583" pname="c" oct="5"
                      accid.ges="s"/>
                  </chord>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1" visible="false">
                  <beam>
                    <space xml:id="d970e3" dur.ges="3"/>
                    <space xml:id="d970e6" dur.ges="1"/>
                  </beam>
                  <space xml:id="d970e9" dur.ges="6"/>
                  <space xml:id="d970e12" dur.ges="2"/>
                </layer>
                <layer n="2">
                  <beam>
                    <chord xml:id="d943e1" dur="8" dots="1"
                      dur.ges="3" stem.dir="up">
                      <note xml:id="d1e6628" pname="e" oct="4"/>
                      <note xml:id="d1e6649" pname="c" oct="4"
                        accid.ges="s"/>
                    </chord>
                    <chord xml:id="d949e1" dur="16" dur.ges="1"
                      stem.dir="up">
                      <note xml:id="d1e6670" pname="d" accid="s"
                        oct="4" accid.ges="s"/>
                      <note xml:id="d1e6695" pname="b" accid="s"
                        oct="3" accid.ges="s"/>
                    </chord>
                  </beam>
                  <chord xml:id="d955e1" dur="4" dots="1" dur.ges="6"
                    stem.dir="up">
                    <note xml:id="d1e6717" pname="f" oct="4"
                      accid.ges="s"/>
                    <note xml:id="d1e6737" pname="d" accid="n" oct="4"
                    />
                  </chord>
                  <chord xml:id="d961e1" dur="8" dur.ges="2"
                    stem.dir="up">
                    <note xml:id="d1e6758" pname="e" oct="4"/>
                    <note xml:id="d1e6776" pname="c" oct="4"
                      accid.ges="s"/>
                  </chord>
                </layer>
                <layer n="3">
                  <note xml:id="d1e6606" pname="a" oct="3" dur="2"
                    dots="1" dur.ges="12" stem.dir="down"/>
                </layer>
              </staff>
              <dynam tstamp="1" place="below" staff="1">pp</dynam>
              <slur tstamp="1" dur="0m+3.5" curvedir="below"
                startid="d1e6628" endid="d1e6758" staff="2"/>
            </measure>
            <measure n="35" xml:id="d1e6804">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e6812" pname="c" oct="5" dur="8"
                      dots="1" dur.ges="3" stem.dir="up" accid.ges="s"/>
                    <note xml:id="d1e6877" pname="c" oct="5" dur="16"
                      dur.ges="1" stem.dir="up" accid.ges="s"/>
                  </beam>
                  <note xml:id="d1e6922" pname="e" oct="4" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <note xml:id="d1e6962" pname="a" oct="4" dur="4"
                    dur.ges="4" stem.dir="up"/>
                </layer>
                <layer n="2">
                  <chord xml:id="d978e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e6837" pname="e" oct="4"/>
                    <note xml:id="d1e6854" pname="c" oct="4"
                      accid.ges="s"/>
                  </chord>
                  <note xml:id="d1e6900" pname="c" oct="4" dur="4"
                    dur.ges="4" stem.dir="down" accid.ges="s"/>
                  <note xml:id="d1e6939" pname="c" oct="4" dur="4"
                    dur.ges="4" stem.dir="down" accid.ges="s"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <chord xml:id="d989e1" dur="4" dur.ges="4"
                    stem.dir="up">
                    <note xml:id="d1e6982" pname="e" oct="3"/>
                    <note xml:id="d1e6999" pname="a" oct="2"/>
                  </chord>
                  <chord xml:id="d995e1" dur="4" dur.ges="4"
                    stem.dir="up">
                    <note xml:id="d1e7017" pname="e" oct="3"/>
                    <note xml:id="d1e7034" pname="a" oct="2"/>
                  </chord>
                  <chord xml:id="d1001e1" dur="4" dur.ges="4"
                    stem.dir="up">
                    <note xml:id="d1e7052" pname="e" oct="3"/>
                    <note xml:id="d1e7069" pname="a" oct="2"/>
                  </chord>
                </layer>
              </staff>
              <dynam tstamp="1" place="below" staff="1">p</dynam>
            </measure>
            <sb/>
            <measure n="36" xml:id="d1e7087">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e7130" pname="c" oct="5" dur="8"
                      dots="1" dur.ges="3" stem.dir="up" accid.ges="s"/>
                    <note xml:id="d1e7152" pname="c" oct="5" dur="16"
                      dur.ges="1" stem.dir="up" accid.ges="s"/>
                  </beam>
                  <note xml:id="d1e7175" pname="e" oct="4" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <note xml:id="d1e7237" pname="a" oct="4" dur="4"
                    dur.ges="4" stem.dir="up"/>
                </layer>
                <layer n="2">
                  <chord xml:id="d1015e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e7090" pname="e" oct="4"/>
                    <note xml:id="d1e7107" pname="c" oct="4"
                      accid.ges="s"/>
                  </chord>
                  <note xml:id="d1e7195" pname="c" oct="4" dur="4"
                    dur.ges="4" stem.dir="down" accid.ges="s"/>
                  <note xml:id="d1e7214" pname="c" oct="4" dur="4"
                    dur.ges="4" stem.dir="down" accid.ges="s"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <chord xml:id="d1027e1" dur="4" dur.ges="4"
                    stem.dir="up">
                    <note xml:id="d1e7257" pname="e" oct="3"/>
                    <note xml:id="d1e7274" pname="a" oct="2"/>
                  </chord>
                  <chord xml:id="d1033e1" dur="4" dur.ges="4"
                    stem.dir="up">
                    <note xml:id="d1e7292" pname="e" oct="3"/>
                    <note xml:id="d1e7309" pname="a" oct="2"/>
                  </chord>
                  <chord xml:id="d1039e1" dur="4" dur.ges="4"
                    stem.dir="up">
                    <note xml:id="d1e7327" pname="e" oct="3"/>
                    <note xml:id="d1e7344" pname="a" oct="2"/>
                  </chord>
                </layer>
              </staff>
            </measure>
            <measure n="37" xml:id="d1e7362">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <chord xml:id="d1053e1" dur="8" dots="1"
                      dur.ges="3" stem.dir="up">
                      <note xml:id="d1e7370" pname="c" oct="5"
                        accid.ges="s"/>
                      <note xml:id="d1e7393" pname="e" oct="4"/>
                    </chord>
                    <chord xml:id="d1059e1" dur="16" dur.ges="1"
                      stem.dir="up">
                      <note xml:id="d1e7417" pname="b" accid="s"
                        oct="4" accid.ges="s"/>
                      <note xml:id="d1e7442" pname="d" accid="s"
                        oct="4" accid.ges="s"/>
                    </chord>
                  </beam>
                  <chord xml:id="d1065e1" dur="4" dots="1" dur.ges="6"
                    stem.dir="up">
                    <note xml:id="d1e7471" pname="d" accid="s" oct="5"
                      accid.ges="s"/>
                    <note xml:id="d1e7493" pname="f" oct="4"
                      accid.ges="s"/>
                  </chord>
                  <chord xml:id="d1071e1" dur="8" dur.ges="2"
                    stem.dir="up">
                    <note xml:id="d1e7519" pname="c" oct="5"
                      accid.ges="s"/>
                    <note xml:id="d1e7540" pname="e" oct="4"/>
                  </chord>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e7561" pname="g" oct="3" dur="8"
                      dots="1" dur.ges="3" stem.dir="up" accid.ges="s"/>
                    <note xml:id="d1e7611" pname="g" oct="3" dur="16"
                      dur.ges="1" stem.dir="up" accid.ges="s"/>
                  </beam>
                  <note xml:id="d1e7658" pname="g" oct="3" dur="2"
                    dur.ges="8" stem.dir="up" accid.ges="s"/>
                </layer>
                <layer n="2">
                  <note xml:id="d1e7587" pname="g" oct="2" dur="4"
                    dur.ges="4" tie="i" stem.dir="down" accid.ges="s"/>
                  <note xml:id="d1e7634" pname="g" oct="2" dur="4"
                    dur.ges="4" tie="t" stem.dir="down" accid.ges="s"/>
                  <note xml:id="d1e7682" pname="c" oct="3" dur="4"
                    dur.ges="4" stem.dir="down" accid.ges="s"/>
                </layer>
              </staff>
              <dynam tstamp="1" place="below" staff="1">mf</dynam>
              <slur tstamp="1" dur="0m+3.5" curvedir="below"
                startid="d1e7370" endid="d1e7519" staff="1"/>
              <slur tstamp="1" dur="0m+2" curvedir="below"
                startid="d1e7561" endid="d1e7658" staff="2"/>
              <hairpin tstamp="1.75" dur="0m+2" form="cres"
                place="below" staff="1"/>
              <hairpin tstamp="2" dur="0m+3.5" form="dim"
                place="below" staff="1"/>
            </measure>
            <measure n="38" xml:id="d1e7701" right="rptend">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <chord xml:id="d1097e1" dur="8" dots="1"
                      dur.ges="3" stem.dir="up">
                      <note xml:id="d1e7711" pname="c" oct="5"
                        accid.ges="s"/>
                      <note xml:id="d1e7734" pname="e" oct="4"/>
                    </chord>
                    <chord xml:id="d1103e1" dur="16" dur.ges="1"
                      stem.dir="up">
                      <note xml:id="d1e7753" pname="b" accid="s"
                        oct="4" accid.ges="s"/>
                      <note xml:id="d1e7778" pname="d" accid="s"
                        oct="4" accid.ges="s"/>
                    </chord>
                  </beam>
                  <chord xml:id="d1109e1" dur="4" dur.ges="4"
                    stem.dir="up">
                    <note xml:id="d1e7807" pname="d" accid="s" oct="5"
                      accid.ges="s"/>
                    <note xml:id="d1e7828" pname="f" oct="4"
                      accid.ges="s"/>
                  </chord>
                  <chord xml:id="d1115e1" dur="4" dur.ges="4"
                    stem.dir="up">
                    <note xml:id="d1e7853" pname="c" oct="5"
                      accid.ges="s"/>
                    <note xml:id="d1e7873" pname="e" oct="4"/>
                  </chord>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e7919" pname="g" oct="3" dur="8"
                      dots="1" dur.ges="3" stem.dir="up" accid.ges="s"/>
                    <note xml:id="d1e7942" pname="g" oct="3" dur="16"
                      dur.ges="1" stem.dir="up" accid.ges="s"/>
                  </beam>
                  <note xml:id="d1e7989" pname="g" oct="3" dur="2"
                    dur.ges="8" stem.dir="up" accid.ges="s"/>
                </layer>
                <layer n="2">
                  <note xml:id="d1e7895" pname="g" oct="2" dur="4"
                    dur.ges="4" tie="i" stem.dir="down" accid.ges="s"/>
                  <note xml:id="d1e7965" pname="g" oct="2" dur="4"
                    dur.ges="4" tie="t" stem.dir="down" accid.ges="s"/>
                  <note xml:id="d1e8012" pname="c" oct="3" dur="4"
                    dur.ges="4" stem.dir="down" accid.ges="s"/>
                </layer>
              </staff>
              <dynam tstamp="1" place="below" staff="1">pp</dynam>
              <hairpin tstamp="1" dur="0m+2" form="cres" place="below"
                staff="1"/>
              <slur tstamp="1" dur="0m+3" curvedir="below"
                startid="d1e7711" endid="d1e7853" staff="1"/>
              <slur tstamp="1" dur="0m+2" curvedir="below"
                startid="d1e7919" endid="d1e7989" staff="2"/>
              <hairpin tstamp="2" dur="0m+3" form="dim" place="below"
                staff="1"/>
            </measure>
          </section>
          <section>
            <measure n="39" xml:id="d1e8035">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e8037" pname="d" accid="n" oct="5"
                      dur="8" dots="1" dur.ges="3" stem.dir="up"/>
                    <note xml:id="d1e8105" pname="d" oct="5" dur="16"
                      dur.ges="1" stem.dir="up"/>
                  </beam>
                  <note xml:id="d1e8166" pname="b" oct="4" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <note xml:id="d1e8224" pname="e" oct="5" dur="4"
                    dur.ges="4" stem.dir="up"/>
                </layer>
                <layer n="2">
                  <chord xml:id="d1142e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e8063" pname="f" oct="4"
                      accid.ges="s"/>
                    <note xml:id="d1e8082" pname="d" accid="n" oct="4"
                    />
                  </chord>
                  <chord xml:id="d1149e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e8126" pname="g" oct="4"
                      accid.ges="s"/>
                    <note xml:id="d1e8145" pname="d" oct="4"/>
                  </chord>
                  <chord xml:id="d1156e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e8183" pname="g" oct="4"
                      accid.ges="s"/>
                    <note xml:id="d1e8203" pname="d" oct="4"/>
                  </chord>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <chord xml:id="d1163e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e8245" pname="b" oct="3"/>
                    <note xml:id="d1e8262" pname="b" oct="2"/>
                  </chord>
                  <chord xml:id="d1169e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e8280" pname="b" oct="3"/>
                    <note xml:id="d1e8297" pname="e" oct="3"/>
                  </chord>
                  <chord xml:id="d1175e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e8315" pname="b" oct="3"/>
                    <note xml:id="d1e8332" pname="e" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <slur tstamp="1" dur="0m+3" curvedir="below"
                startid="d1e8037" endid="d1e8224" staff="1"/>
            </measure>
            <measure n="40" xml:id="d1e8350">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e8392" pname="c" oct="5" dur="8"
                      dots="1" dur.ges="3" stem.dir="up" accid.ges="s"/>
                    <note xml:id="d1e8414" pname="c" oct="5" dur="16"
                      dur.ges="1" stem.dir="up" accid.ges="s"/>
                  </beam>
                  <note xml:id="d1e8459" pname="e" oct="4" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <note xml:id="d1e8498" pname="a" oct="4" dur="4"
                    dur.ges="4" stem.dir="up"/>
                </layer>
                <layer n="2">
                  <chord xml:id="d1191e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e8352" pname="e" oct="4"/>
                    <note xml:id="d1e8369" pname="c" oct="4"
                      accid.ges="s"/>
                  </chord>
                  <note xml:id="d1e8437" pname="c" oct="4" dur="4"
                    dur.ges="4" stem.dir="down" accid.ges="s"/>
                  <note xml:id="d1e8476" pname="c" oct="4" dur="4"
                    dur.ges="4" stem.dir="down" accid.ges="s"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <chord xml:id="d1203e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e8519" pname="a" oct="3"/>
                    <note xml:id="d1e8536" pname="e" oct="3"/>
                    <note xml:id="d1e8554" pname="a" oct="2"/>
                  </chord>
                  <chord xml:id="d1210e1" dur="4" dur.ges="4"
                    stem.dir="up">
                    <note xml:id="d1e8572" pname="e" oct="3"/>
                    <note xml:id="d1e8589" pname="a" oct="2"/>
                  </chord>
                  <chord xml:id="d1216e1" dur="4" dur.ges="4"
                    stem.dir="up">
                    <note xml:id="d1e8607" pname="e" oct="3"/>
                    <note xml:id="d1e8624" pname="a" oct="2"/>
                  </chord>
                </layer>
              </staff>
            </measure>
            <sb/>
            <measure n="41" xml:id="d1e8642">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e8650" pname="b" oct="4" dur="8"
                      dots="1" dur.ges="3" stem.dir="up"/>
                    <note xml:id="d1e8722" pname="b" oct="4" dur="16"
                      dur.ges="1" stem.dir="up"/>
                  </beam>
                  <note xml:id="d1e8743" pname="b" oct="4" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <note xml:id="d1e8803" pname="b" oct="4" dur="4"
                    dur.ges="4" stem.dir="up"/>
                </layer>
                <layer n="2">
                  <chord xml:id="d1231e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e8673" pname="f" oct="4"
                      accid.ges="s"/>
                    <note xml:id="d1e8692" pname="d" accid="s" oct="4"
                      accid.ges="s"/>
                  </chord>
                  <chord xml:id="d1239e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e8764" pname="f" accid="n" oct="4"/>
                    <note xml:id="d1e8783" pname="d" accid="n" oct="4"
                    />
                  </chord>
                  <chord xml:id="d1246e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e8823" pname="e" oct="4"/>
                    <note xml:id="d1e8840" pname="d" oct="4"/>
                  </chord>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <chord xml:id="d1252e1" dur="4" dur.ges="4"
                    stem.dir="up">
                    <note xml:id="d1e8861" pname="f" oct="3"
                      accid.ges="s"/>
                    <note xml:id="d1e8880" pname="a" oct="2"/>
                  </chord>
                  <chord xml:id="d1258e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e8898" pname="g" oct="3"
                      accid.ges="s"/>
                    <note xml:id="d1e8917" pname="a" oct="2"/>
                  </chord>
                  <chord xml:id="d1264e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e8936" pname="g" oct="3"
                      accid.ges="s"/>
                    <note xml:id="d1e8955" pname="a" oct="2"/>
                  </chord>
                </layer>
              </staff>
              <hairpin tstamp="1" dur="0m+1.75" form="cres"
                place="below" staff="1"/>
            </measure>
            <measure n="42" xml:id="d1e8973">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e9015" pname="c" oct="5" dur="8"
                      dots="1" dur.ges="3" stem.dir="up" accid.ges="s"/>
                    <note xml:id="d1e9037" pname="c" oct="5" dur="16"
                      dur.ges="1" stem.dir="up" accid.ges="s"/>
                  </beam>
                  <note xml:id="d1e9082" pname="e" oct="4" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <note xml:id="d1e9121" pname="a" oct="4" dur="4"
                    dur.ges="4" stem.dir="up"/>
                </layer>
                <layer n="2">
                  <chord xml:id="d1279e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e8975" pname="e" oct="4"/>
                    <note xml:id="d1e8992" pname="c" oct="4"
                      accid.ges="s"/>
                  </chord>
                  <note xml:id="d1e9060" pname="c" oct="4" dur="4"
                    dur.ges="4" stem.dir="down" accid.ges="s"/>
                  <note xml:id="d1e9099" pname="c" oct="4" dur="4"
                    dur.ges="4" stem.dir="down" accid.ges="s"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <chord xml:id="d1291e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e9142" pname="a" oct="3"/>
                    <note xml:id="d1e9159" pname="a" oct="2"/>
                  </chord>
                  <chord xml:id="d1297e1" dur="4" dur.ges="4"
                    stem.dir="up">
                    <note xml:id="d1e9177" pname="e" oct="3"/>
                    <note xml:id="d1e9194" pname="a" oct="2"/>
                  </chord>
                  <chord xml:id="d1303e1" dur="4" dur.ges="4"
                    stem.dir="up">
                    <note xml:id="d1e9212" pname="e" oct="3"/>
                    <note xml:id="d1e9229" pname="a" oct="2"/>
                  </chord>
                </layer>
              </staff>
            </measure>
            <measure n="43" xml:id="d1e9248">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e9293" pname="d" oct="5" dur="8"
                      dots="1" dur.ges="3" stem.dir="up"/>
                    <note xml:id="d1e9318" pname="d" oct="5" dur="16"
                      dur.ges="1" stem.dir="up"/>
                  </beam>
                  <note xml:id="d1e9339" pname="b" oct="4" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <note xml:id="d1e9395" pname="e" oct="5" dur="4"
                    dur.ges="4" stem.dir="up"/>
                </layer>
                <layer n="2">
                  <chord xml:id="d1317e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e9255" pname="a" oct="4"/>
                    <note xml:id="d1e9272" pname="d" oct="4"/>
                  </chord>
                  <chord xml:id="d1326e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e9359" pname="a" oct="4"/>
                    <note xml:id="d1e9376" pname="d" oct="4"/>
                  </chord>
                  <chord xml:id="d1333e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e9415" pname="g" oct="4"
                      accid.ges="s"/>
                    <note xml:id="d1e9434" pname="d" oct="4"/>
                  </chord>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <chord xml:id="d1339e1" dur="4" dur.ges="4"
                    stem.dir="up">
                    <note xml:id="d1e9455" pname="f" oct="3"
                      artic="ten" accid.ges="s"/>
                    <note xml:id="d1e9476" pname="a" oct="2"/>
                  </chord>
                  <chord xml:id="d1345e1" dur="4" dur.ges="4"
                    stem.dir="up">
                    <note xml:id="d1e9494" pname="f" accid="n" oct="3"/>
                    <note xml:id="d1e9513" pname="a" oct="2"/>
                  </chord>
                  <chord xml:id="d1351e1" dur="4" dur.ges="4"
                    stem.dir="up">
                    <note xml:id="d1e9531" pname="e" oct="3"/>
                    <note xml:id="d1e9548" pname="a" oct="2"/>
                  </chord>
                </layer>
              </staff>
              <hairpin tstamp="1" dur="0m+1.75" form="dim"
                place="below" staff="1"/>
            </measure>
            <measure n="44" xml:id="d1e9566">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e9608" pname="c" oct="5" dur="8"
                      dots="1" dur.ges="3" stem.dir="up" accid.ges="s"/>
                    <note xml:id="d1e9630" pname="c" oct="5" dur="16"
                      dur.ges="1" stem.dir="up" accid.ges="s"/>
                  </beam>
                  <note xml:id="d1e9653" pname="e" oct="4" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <note xml:id="d1e9733" pname="a" oct="4" dur="4"
                    dur.ges="4" stem.dir="up"/>
                </layer>
                <layer n="2">
                  <chord xml:id="d1366e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e9568" pname="e" oct="4"/>
                    <note xml:id="d1e9585" pname="c" oct="4"
                      accid.ges="s"/>
                  </chord>
                  <note xml:id="d1e9673" pname="c" oct="4" dur="4"
                    dur.ges="4" stem.dir="down" accid.ges="s"/>
                  <chord xml:id="d1376e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e9692" pname="e" oct="4"/>
                    <note xml:id="d1e9709" pname="c" oct="4"
                      accid.ges="s"/>
                  </chord>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <chord xml:id="d1383e1" dur="4" dur.ges="4"
                    stem.dir="up">
                    <note xml:id="d1e9753" pname="e" oct="3"/>
                    <note xml:id="d1e9770" pname="a" oct="2"/>
                  </chord>
                  <chord xml:id="d1389e1" dur="4" dur.ges="4"
                    stem.dir="up">
                    <note xml:id="d1e9788" pname="e" oct="3"/>
                    <note xml:id="d1e9805" pname="a" oct="2"/>
                  </chord>
                  <chord xml:id="d1395e1" dur="4" dur.ges="4"
                    stem.dir="up">
                    <note xml:id="d1e9823" pname="e" oct="3"/>
                    <note xml:id="d1e9840" pname="a" oct="2"/>
                  </chord>
                </layer>
              </staff>
            </measure>
            <measure n="45" xml:id="d1e9858">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e9860" pname="b" oct="4" dur="8"
                      dots="1" dur.ges="3" stem.dir="up"/>
                    <note xml:id="d1e9929" pname="b" oct="4" dur="16"
                      dur.ges="1" stem.dir="up"/>
                  </beam>
                  <note xml:id="d1e9992" pname="b" oct="4" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <note xml:id="d1e10009" pname="b" oct="4" dur="4"
                    dur.ges="4" stem.dir="up"/>
                </layer>
                <layer n="2">
                  <chord xml:id="d1410e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e9883" pname="f" oct="4"
                      artic="stacc" accid.ges="s"/>
                    <note xml:id="d1e9904" pname="d" accid="s" oct="4"
                      accid.ges="s"/>
                  </chord>
                  <chord xml:id="d1417e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e9950" pname="f" accid="n" oct="4"/>
                    <note xml:id="d1e9969" pname="d" accid="n" oct="4"
                    />
                  </chord>
                  <chord xml:id="d1425e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e10030" pname="e" oct="4"/>
                    <note xml:id="d1e10047" pname="d" oct="4"/>
                  </chord>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <chord xml:id="d1431e1" dur="4" dur.ges="4"
                    stem.dir="up">
                    <note xml:id="d1e10068" pname="f" accid="s"
                      oct="3" accid.ges="s"/>
                    <note xml:id="d1e10089" pname="a" oct="2"/>
                  </chord>
                  <chord xml:id="d1437e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e10107" pname="g" oct="3"
                      accid.ges="s"/>
                    <note xml:id="d1e10126" pname="a" oct="2"/>
                  </chord>
                  <chord xml:id="d1443e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e10144" pname="g" oct="3"
                      accid.ges="s"/>
                    <note xml:id="d1e10163" pname="a" oct="2"/>
                  </chord>
                </layer>
              </staff>
            </measure>
            <measure n="46" xml:id="d1e10181" right="dbl">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e10183" pname="c" oct="5" dur="8"
                      dots="1" dur.ges="3" stem.dir="up" accid.ges="s"/>
                    <note xml:id="d1e10248" pname="c" oct="5" dur="16"
                      dur.ges="1" stem.dir="up" accid.ges="s"/>
                  </beam>
                  <rest vo="6" xml:id="d1e10311" dur="4" dur.ges="4"/>
                  <rest vo="8" xml:id="d1e10326" dur="4" dur.ges="4"/>
                </layer>
                <layer n="2">
                  <chord xml:id="d1458e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e10208" pname="e" oct="4"/>
                    <note xml:id="d1e10225" pname="c" oct="4"
                      accid.ges="s"/>
                  </chord>
                  <chord xml:id="d1465e1" dur="4" dur.ges="4"
                    stem.dir="up">
                    <note xml:id="d1e10271" pname="e" oct="4"/>
                    <note xml:id="d1e10288" pname="c" oct="4"
                      accid.ges="s"/>
                  </chord>
                  <chord xml:id="d1471e1" dur="4" dur.ges="4"
                    stem.dir="up">
                    <note xml:id="d1e10345" pname="a" oct="4"/>
                    <note xml:id="d1e10362" pname="c" oct="4"
                      accid.ges="s"/>
                  </chord>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <chord xml:id="d1477e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e10385" pname="a" oct="3"/>
                    <note xml:id="d1e10402" pname="a" oct="2"/>
                  </chord>
                  <chord xml:id="d1483e1" dur="4" dur.ges="4"
                    stem.dir="up">
                    <note xml:id="d1e10420" pname="e" oct="3"/>
                    <note xml:id="d1e10437" pname="a" oct="2"/>
                  </chord>
                  <chord xml:id="d1489e1" dur="4" dur.ges="4"
                    stem.dir="up">
                    <note xml:id="d1e10455" pname="e" oct="3"/>
                    <note xml:id="d1e10472" pname="a" oct="2"/>
                  </chord>
                </layer>
              </staff>
            </measure>
          </section>
          <section>
            <sb/>
            <scoredef key.sig="0"/>
            <measure n="47" xml:id="d1e10493">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e10500" pname="e" oct="5" dur="8"
                      dots="1" dur.ges="3" stem.dir="down"/>
                    <note xml:id="d1e10520" pname="e" oct="5" dur="16"
                      dur.ges="1" stem.dir="down"/>
                  </beam>
                  <note xml:id="d1e10541" pname="c" oct="5" dur="4"
                    dur.ges="4" stem.dir="down"/>
                  <note xml:id="d1e10558" pname="d" accid="s" oct="5"
                    dur="4" dur.ges="4" stem.dir="down" accid.ges="s"
                  />
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e10584" pname="a" oct="1" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d1508e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e10601" pname="c" oct="4"/>
                    <note xml:id="d1e10618" pname="e" oct="3"/>
                  </chord>
                  <chord xml:id="d1514e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e10636" pname="b" oct="3"/>
                    <note xml:id="d1e10654" pname="e" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <trill tstamp="3" place="above" staff="1"
                startid="d1e10558"/>
            </measure>
            <measure n="48" xml:id="d1e10672">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e10674" pname="e" oct="5" dur="8"
                      dots="1" dur.ges="3" stem.dir="down"/>
                    <note xml:id="d1e10695" pname="e" oct="5" dur="16"
                      dur.ges="1" stem.dir="down"/>
                  </beam>
                  <note xml:id="d1e10716" pname="a" oct="4" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <note xml:id="d1e10733" pname="c" oct="5" dur="4"
                    dur.ges="4" stem.dir="down"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e10754" pname="a" oct="2" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d1533e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e10771" pname="c" oct="4"/>
                    <note xml:id="d1e10788" pname="e" oct="3"/>
                  </chord>
                  <chord xml:id="d1539e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e10806" pname="c" oct="4"/>
                    <note xml:id="d1e10823" pname="e" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <slur tstamp="1" dur="0m+3" curvedir="above"
                startid="d1e10674" endid="d1e10733" staff="1"/>
            </measure>
            <measure n="49" xml:id="d1e10841">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e10843" pname="b" oct="4" dur="8"
                      dots="1" dur.ges="3" stem.dir="down"/>
                    <note xml:id="d1e10863" pname="b" oct="4" dur="16"
                      dur.ges="1" stem.dir="down"/>
                  </beam>
                  <note xml:id="d1e10884" pname="f" accid="s" oct="4"
                    dur="4" dur.ges="4" stem.dir="up" accid.ges="s"/>
                  <note xml:id="d1e10905" pname="g" accid="s" oct="4"
                    dur="4" dur.ges="4" stem.dir="up" accid.ges="s"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e10931" pname="a" oct="2" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d1560e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e10948" pname="d" oct="4"/>
                    <note xml:id="d1e10965" pname="e" oct="3"/>
                  </chord>
                  <chord xml:id="d1566e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e10983" pname="d" oct="4"/>
                    <note xml:id="d1e11000" pname="e" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <trill tstamp="3" place="above" staff="1"
                startid="d1e10905"/>
            </measure>
            <measure n="50" xml:id="d1e11018">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e11020" pname="a" oct="4" dur="8"
                      artic="stacciss" dur.ges="2" stem.dir="up"/>
                    <rest xml:id="d1e11041" dur="16" dur.ges="1"/>
                    <note xml:id="d1e11057" pname="e" oct="4" dur="16"
                      dur.ges="1" stem.dir="up"/>
                    <note xml:id="d1e11079" pname="a" oct="4" dur="8"
                      artic="stacciss" dur.ges="2" stem.dir="up"/>
                    <rest xml:id="d1e11101" dur="16" dur.ges="1"/>
                    <note xml:id="d1e11112" pname="e" oct="4" dur="16"
                      dur.ges="1" stem.dir="up"/>
                    <note xml:id="d1e11134" pname="a" oct="4" dur="8"
                      artic="stacciss" dur.ges="2" stem.dir="up"/>
                    <rest xml:id="d1e11156" dur="16" dur.ges="1"/>
                    <note xml:id="d1e11172" pname="c" oct="5" dur="16"
                      dur.ges="1" stem.dir="up"/>
                  </beam>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e11198" pname="a" oct="2" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d1587e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e11215" pname="c" oct="4"/>
                    <note xml:id="d1e11232" pname="e" oct="3"/>
                  </chord>
                  <chord xml:id="d1593e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e11250" pname="c" oct="4"/>
                    <note xml:id="d1e11267" pname="e" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <hairpin tstamp="1.75" dur="0m+3.75" form="cres"
                place="below" staff="1"/>
              <slur tstamp="1.75" dur="0m+2" curvedir="below"
                startid="d1e11057" endid="d1e11079" staff="1"/>
              <slur tstamp="2.75" dur="0m+3" curvedir="below"
                startid="d1e11112" endid="d1e11134" staff="1"/>
              <slur tstamp="3.75" dur="1m+1" curvedir="below"
                startid="d1e11172" endid="d1e11287" staff="1"/>
            </measure>
            <measure n="51" xml:id="d1e11285">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e11287" pname="e" oct="5" dur="8"
                      artic="stacciss" dur.ges="2" stem.dir="down"/>
                    <rest xml:id="d1e11309" dur="16" dur.ges="1"/>
                    <note xml:id="d1e11320" pname="e" oct="5" dur="16"
                      dur.ges="1" stem.dir="down"/>
                  </beam>
                  <note xml:id="d1e11342" pname="c" oct="5" dur="4"
                    dur.ges="4" stem.dir="down"/>
                  <note xml:id="d1e11360" pname="d" accid="s" oct="5"
                    dur="4" artic="acc" dur.ges="4" stem.dir="down"
                    accid.ges="s"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e11388" pname="a" oct="2" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d1621e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e11405" pname="c" oct="4"/>
                    <note xml:id="d1e11422" pname="e" oct="3"/>
                  </chord>
                  <chord xml:id="d1627e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e11440" pname="b" oct="3"/>
                    <note xml:id="d1e11457" pname="e" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <slur tstamp="1.75" dur="0m+2" curvedir="above"
                startid="d1e11320" endid="d1e11342" staff="1"/>
              <trill tstamp="3" place="above" staff="1"
                startid="d1e11360"/>
            </measure>
            <sb/>
            <measure n="52" xml:id="d1e11475">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e11478" pname="e" oct="5" dur="8"
                      dots="1" dur.ges="3" stem.dir="down"/>
                    <note xml:id="d1e11499" pname="e" oct="5" dur="16"
                      dur.ges="1" stem.dir="down"/>
                  </beam>
                  <note xml:id="d1e11520" pname="a" oct="4" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <note xml:id="d1e11537" pname="c" oct="5" dur="4"
                    dur.ges="4" stem.dir="down"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e11558" pname="a" oct="2" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d1648e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e11575" pname="c" oct="4"/>
                    <note xml:id="d1e11592" pname="e" oct="3"/>
                  </chord>
                  <chord xml:id="d1654e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e11610" pname="c" oct="4"/>
                    <note xml:id="d1e11627" pname="e" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <slur tstamp="1" dur="0m+3" curvedir="above"
                startid="d1e11478" endid="d1e11537" staff="1"/>
            </measure>
            <measure n="53" xml:id="d1e11645">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e11647" pname="b" oct="4" dur="8"
                      dots="1" dur.ges="3" stem.dir="down"/>
                    <note xml:id="d1e11667" pname="b" oct="4" dur="16"
                      dur.ges="1" stem.dir="down"/>
                  </beam>
                  <note xml:id="d1e11688" pname="f" accid="s" oct="4"
                    dur="4" dur.ges="4" stem.dir="up" accid.ges="s"/>
                  <note xml:id="d1e11709" pname="g" accid="s" oct="4"
                    dur="4" dur.ges="4" stem.dir="up" accid.ges="s"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e11735" pname="a" oct="2" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d1675e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e11752" pname="d" oct="4"/>
                    <note xml:id="d1e11769" pname="e" oct="3"/>
                  </chord>
                  <chord xml:id="d1681e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e11787" pname="d" oct="4"/>
                    <note xml:id="d1e11804" pname="e" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <trill tstamp="3" place="above" staff="1"
                startid="d1e11709"/>
            </measure>
            <measure n="54" xml:id="d1e11823">
              <staff n="1">
                <layer n="1">
                  <note xml:id="d1e11825" pname="a" oct="5" dur="4"
                    dur.ges="4" stem.dir="down"/>
                  <rest xml:id="d1e11842" dur="8" dots="1" dur.ges="3"/>
                  <beam>
                    <note xml:id="d1e11854" pname="g" accid="n"
                      oct="4" dur="16" dur.ges="1" stem.dir="down"/>
                    <note xml:id="d1e11878" pname="c" oct="5" dur="8"
                      dots="1" dur.ges="3" stem.dir="down"/>
                    <note xml:id="d1e11898" pname="e" oct="5" dur="16"
                      dur.ges="1" stem.dir="down"/>
                  </beam>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <chord xml:id="d1699e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e11922" pname="c" oct="4"/>
                    <note xml:id="d1e11939" pname="a" oct="3"/>
                  </chord>
                  <rest xml:id="d1e11957" dur="4" dur.ges="4"/>
                  <rest xml:id="d1e11968" dur="4" dur.ges="4"/>
                </layer>
              </staff>
              <slur tstamp="2.75" dur="1m+1" curvedir="above"
                startid="d1e11854" endid="d1e11981" staff="1"/>
            </measure>
            <measure n="55" xml:id="d1e11979">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e11981" pname="g" oct="5" dur="8"
                      dots="1" dur.ges="3" stem.dir="down"/>
                    <note xml:id="d1e12002" pname="g" oct="5" dur="16"
                      dur.ges="1" stem.dir="down"/>
                  </beam>
                  <note xml:id="d1e12023" pname="e" oct="5" dur="4"
                    dur.ges="4" stem.dir="down"/>
                  <note xml:id="d1e12040" pname="f" accid="s" oct="5"
                    dur="4" artic="acc" dur.ges="4" stem.dir="down"
                    accid.ges="s"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e12066" pname="c" oct="3" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d1720e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e12083" pname="e" oct="4"/>
                    <note xml:id="d1e12100" pname="g" oct="3"/>
                  </chord>
                  <chord xml:id="d1726e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e12118" pname="d" accid="s"
                      oct="4" artic="acc" accid.ges="s"/>
                    <note xml:id="d1e12141" pname="g" oct="3"/>
                  </chord>
                </layer>
              </staff>
            </measure>
            <measure n="56" xml:id="d1e12159">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e12161" pname="g" oct="5" dur="8"
                      dots="1" dur.ges="3" stem.dir="down"/>
                    <note xml:id="d1e12181" pname="g" oct="5" dur="16"
                      dur.ges="1" stem.dir="down"/>
                  </beam>
                  <note xml:id="d1e12202" pname="e" oct="5" dur="4"
                    dur.ges="4" stem.dir="down"/>
                  <note xml:id="d1e12219" pname="f" accid="s" oct="5"
                    dur="4" artic="acc" dur.ges="4" stem.dir="down"
                    accid.ges="s"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e12245" pname="c" oct="3" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d1745e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e12262" pname="e" oct="4"/>
                    <note xml:id="d1e12279" pname="g" oct="3"/>
                  </chord>
                  <chord xml:id="d1751e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e12297" pname="d" accid="s"
                      oct="4" artic="acc" accid.ges="s"/>
                    <note xml:id="d1e12320" pname="g" oct="3"/>
                  </chord>
                </layer>
              </staff>
            </measure>
            <sb/>
            <measure n="57" xml:id="d1e12338">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e12341" pname="g" oct="5" dur="8"
                      dur.ges="2" stem.dir="down"/>
                    <rest vo="3" xml:id="d1e12360" dur="16"
                      dur.ges="1"/>
                    <note xml:id="d1e12375" pname="g" oct="5" dur="16"
                      dur.ges="1" stem.dir="down"/>
                  </beam>
                  <note xml:id="d1e12397" pname="c" oct="5" dur="4"
                    dur.ges="4" stem.dir="down"/>
                  <note xml:id="d1e12415" pname="d" oct="5" dur="4"
                    dur.ges="4" stem.dir="down"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e12435" pname="c" oct="3" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d1770e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e12452" pname="e" oct="4"/>
                    <note xml:id="d1e12469" pname="g" oct="3"/>
                  </chord>
                  <chord xml:id="d1776e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e12487" pname="f" oct="4"
                      artic="acc"/>
                    <note xml:id="d1e12507" pname="g" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <slur tstamp="1.75" dur="0m+2" curvedir="above"
                startid="d1e12375" endid="d1e12397" staff="1"/>
            </measure>
            <measure n="58" xml:id="d1e12525">
              <staff n="1">
                <layer n="1">
                  <note xml:id="d1e12527" pname="e" oct="5" dur="2"
                    dots="1" dur.ges="12" stem.dir="down"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e12548" pname="c" oct="3" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d1794e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e12565" pname="e" oct="4"/>
                    <note xml:id="d1e12583" pname="g" oct="3"/>
                  </chord>
                  <chord xml:id="d1800e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e12601" pname="d" oct="4"/>
                    <note xml:id="d1e12619" pname="g" accid="s"
                      oct="3" accid.ges="s"/>
                    <note xml:id="d1e12641" pname="e" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <slur tstamp="2" dur="0m+3" curvedir="above"
                startid="d1e12565" endid="d1e12601" staff="2"/>
            </measure>
            <measure n="59" xml:id="d1e12659">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e12661" pname="e" oct="5" dur="8"
                      dots="1" dur.ges="3" stem.dir="down"/>
                    <note xml:id="d1e12681" pname="e" oct="5" dur="16"
                      dur.ges="1" stem.dir="down"/>
                  </beam>
                  <note xml:id="d1e12702" pname="c" oct="5" dur="4"
                    dur.ges="4" stem.dir="down"/>
                  <note xml:id="d1e12719" pname="d" accid="s" oct="5"
                    dur="4" artic="acc" dur.ges="4" stem.dir="down"
                    accid.ges="s"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e12747" pname="a" oct="1" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d1822e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e12764" pname="c" oct="4"/>
                    <note xml:id="d1e12781" pname="e" oct="3"/>
                  </chord>
                  <chord xml:id="d1828e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e12799" pname="b" oct="3"/>
                    <note xml:id="d1e12816" pname="e" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <trill tstamp="3" place="above" staff="1"
                startid="d1e12719"/>
            </measure>
            <measure n="60" xml:id="d1e12834">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e12836" pname="e" oct="5" dur="8"
                      dots="1" dur.ges="3" stem.dir="down"/>
                    <note xml:id="d1e12857" pname="e" oct="5" dur="16"
                      dur.ges="1" stem.dir="down"/>
                  </beam>
                  <note xml:id="d1e12878" pname="a" oct="4" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <note xml:id="d1e12895" pname="c" oct="5" dur="4"
                    dur.ges="4" stem.dir="down"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e12916" pname="a" oct="2" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d1847e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e12933" pname="c" oct="4"/>
                    <note xml:id="d1e12950" pname="e" oct="3"/>
                  </chord>
                  <chord xml:id="d1853e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e12968" pname="c" oct="4"/>
                    <note xml:id="d1e12985" pname="e" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <slur tstamp="1" dur="0m+3" curvedir="above"
                startid="d1e12836" endid="d1e12895" staff="1"/>
            </measure>
            <measure n="61" xml:id="d1e13003">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e13005" pname="b" oct="4" dur="8"
                      dots="1" dur.ges="3" stem.dir="down"/>
                    <note xml:id="d1e13025" pname="b" oct="4" dur="16"
                      dur.ges="1" stem.dir="down"/>
                  </beam>
                  <note xml:id="d1e13046" pname="f" accid="s" oct="4"
                    dur="4" dur.ges="4" stem.dir="up" accid.ges="s"/>
                  <note xml:id="d1e13067" pname="g" accid="s" oct="4"
                    dur="4" dur.ges="4" stem.dir="up" accid.ges="s"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e13093" pname="a" oct="2" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d1874e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e13110" pname="d" oct="4"/>
                    <note xml:id="d1e13127" pname="e" oct="3"/>
                  </chord>
                  <chord xml:id="d1880e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e13145" pname="d" oct="4"/>
                    <note xml:id="d1e13162" pname="e" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <trill tstamp="3" place="above" staff="1"
                startid="d1e13067"/>
            </measure>
            <sb/>
            <measure n="62" xml:id="d1e13180">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e13183" pname="a" oct="4" dur="8"
                      artic="stacciss" dur.ges="2" stem.dir="up"/>
                    <rest xml:id="d1e13204" dur="16" dur.ges="1"/>
                    <note xml:id="d1e13215" pname="e" oct="4" dur="16"
                      dur.ges="1" stem.dir="up"/>
                    <note xml:id="d1e13237" pname="a" oct="4" dur="8"
                      artic="stacciss" dur.ges="2" stem.dir="up"/>
                    <rest xml:id="d1e13259" dur="16" dur.ges="1"/>
                    <note xml:id="d1e13270" pname="e" oct="4" dur="16"
                      dur.ges="1" stem.dir="up"/>
                    <note xml:id="d1e13292" pname="a" oct="4" dur="8"
                      artic="stacciss" dur.ges="2" stem.dir="up"/>
                    <rest xml:id="d1e13314" dur="16" dur.ges="1"/>
                    <note xml:id="d1e13325" pname="c" oct="5" dur="16"
                      dur.ges="1" stem.dir="up"/>
                  </beam>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e13351" pname="a" oct="2" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d1901e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e13368" pname="c" oct="4"/>
                    <note xml:id="d1e13385" pname="e" oct="3"/>
                  </chord>
                  <chord xml:id="d1907e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e13403" pname="c" oct="4"/>
                    <note xml:id="d1e13420" pname="e" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <slur tstamp="1.75" dur="0m+2" curvedir="below"
                startid="d1e13215" endid="d1e13237" staff="1"/>
              <slur tstamp="2.75" dur="0m+3" curvedir="below"
                startid="d1e13270" endid="d1e13292" staff="1"/>
              <slur tstamp="3.75" dur="1m+1" curvedir="below"
                startid="d1e13325" endid="d1e13440" staff="1"/>
            </measure>
            <measure n="63" xml:id="d1e13438">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e13440" pname="e" oct="5" dur="8"
                      artic="stacciss" dur.ges="2" stem.dir="down"/>
                    <rest xml:id="d1e13462" dur="16" dur.ges="1"/>
                    <note xml:id="d1e13473" pname="e" oct="5" dur="16"
                      dur.ges="1" stem.dir="down"/>
                  </beam>
                  <note xml:id="d1e13495" pname="c" oct="5" dur="4"
                    dur.ges="4" stem.dir="down"/>
                  <note xml:id="d1e13513" pname="d" accid="s" oct="5"
                    dur="4" artic="acc" dur.ges="4" stem.dir="down"
                    accid.ges="s"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e13541" pname="a" oct="2" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d1934e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e13558" pname="c" oct="4"/>
                    <note xml:id="d1e13575" pname="e" oct="3"/>
                  </chord>
                  <chord xml:id="d1940e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e13593" pname="b" oct="3"/>
                    <note xml:id="d1e13610" pname="e" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <slur tstamp="1.75" dur="0m+2" curvedir="above"
                startid="d1e13473" endid="d1e13495" staff="1"/>
              <trill tstamp="3" place="above" staff="1"
                startid="d1e13513"/>
            </measure>
            <measure n="64" xml:id="d1e13628">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e13630" pname="e" oct="5" dur="8"
                      dots="1" dur.ges="3" stem.dir="down"/>
                    <note xml:id="d1e13650" pname="e" oct="5" dur="16"
                      dur.ges="1" stem.dir="down"/>
                  </beam>
                  <note xml:id="d1e13671" pname="a" oct="4" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <note xml:id="d1e13688" pname="c" oct="5" dur="4"
                    dur.ges="4" stem.dir="down"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e13708" pname="a" oct="2" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d1961e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e13725" pname="c" oct="4"/>
                    <note xml:id="d1e13742" pname="e" oct="3"/>
                  </chord>
                  <chord xml:id="d1967e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e13760" pname="c" oct="4"/>
                    <note xml:id="d1e13777" pname="e" oct="3"/>
                  </chord>
                </layer>
              </staff>
            </measure>
            <measure n="65" xml:id="d1e13796">
              <staff n="1">
                <layer n="1">
                  <beam>
                    <note xml:id="d1e13798" pname="b" oct="4" dur="8"
                      dots="1" dur.ges="3" stem.dir="down"/>
                    <note xml:id="d1e13818" pname="b" oct="4" dur="16"
                      dur.ges="1" stem.dir="down"/>
                  </beam>
                  <note xml:id="d1e13839" pname="f" accid="s" oct="4"
                    dur="4" dur.ges="4" stem.dir="up" accid.ges="s"/>
                  <note xml:id="d1e13860" pname="g" accid="s" oct="4"
                    dur="4" dur.ges="4" stem.dir="up" accid.ges="s"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e13886" pname="a" oct="2" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d1986e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e13903" pname="d" oct="4"/>
                    <note xml:id="d1e13920" pname="e" oct="3"/>
                  </chord>
                  <chord xml:id="d1992e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e13938" pname="d" oct="4"/>
                    <note xml:id="d1e13955" pname="e" oct="3"/>
                  </chord>
                </layer>
              </staff>
              <trill tstamp="3" place="above" staff="1"
                startid="d1e13860"/>
            </measure>
            <measure n="66" xml:id="d1e13973" right="end">
              <staff n="1">
                <layer n="1">
                  <note xml:id="d1e13975" pname="a" oct="5" dur="4"
                    dur.ges="4" stem.dir="down"/>
                  <rest xml:id="d1e13992" dur="4" dur.ges="4"/>
                  <rest xml:id="d1e14003" dur="4" dur.ges="4"/>
                </layer>
              </staff>
              <staff n="2">
                <layer n="1">
                  <note xml:id="d1e14017" pname="a" oct="2" dur="4"
                    dur.ges="4" stem.dir="up"/>
                  <chord xml:id="d2008e1" dur="4" dur.ges="4"
                    stem.dir="down">
                    <note xml:id="d1e14034" pname="c" oct="4"/>
                    <note xml:id="d1e14051" pname="e" oct="3"/>
                  </chord>
                  <rest xml:id="d1e14069" dur="4" dur.ges="4"/>
                </layer>
              </staff>
            </measure>
          </section>
        </score>
      </mdiv>
    </body>
  </music>
</mei>
"""