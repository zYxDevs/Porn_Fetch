<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE TS>
<TS version="2.1" language="fr" sourcelanguage="en_US">
<context>
    <name>KeyboardShortcuts</name>
    <message>
        <location filename="../form_keyboard_shortcuts.ui" line="32"/>
        <source>Keyboard Shortcuts</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_keyboard_shortcuts.ui" line="70"/>
        <source>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;meta charset=&quot;utf-8&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
hr { height: 1px; border-width: 0; }
li.unchecked::marker { content: &quot;\2610&quot;; }
li.checked::marker { content: &quot;\2612&quot;; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:&apos;Sans Serif&apos;; font-size:9pt; font-weight:400; font-style:normal;&quot;&gt;
&lt;p align=&quot;center&quot; style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-size:14pt; font-weight:700;&quot;&gt;Keyboard Shortcuts&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; font-weight:700;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;CTRL + Q     Closes the application&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;CTRL + E      Exports all current video URLs from the tree widget into a .txt file &lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;CTRL + T      Downloads all videos in the tree widget (same as clicking the button)&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;CTRL + A     Quickly enables the anonymous mode (temporarily)&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;CTRL + S     Saves Porn Fetch settings&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;CTRL + X     Selects all items in the tree widget as checked&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;CTRL + Z     Unchecks all items in the tree widget&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;   &lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation type="unfinished"></translation>
    </message>
</context>
<context>
    <name>PornFetch</name>
    <message>
        <location filename="../../../main.py" line="1123"/>
        <source>You are running on Android! You can not install Porn Fetch</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../../../main.py" line="1127"/>
        <source>Porn Fetch installation successful!</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../../../main.py" line="1130"/>
        <source>Porn Fetch installation failed, because of: {result[1]}</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../../../main.py" line="1550"/>
        <source>Saved User Settings, please restart Porn Fetch!</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../../../main.py" line="1581"/>
        <source>
!!! ONLY SOCKS5 IS SUPPORTED !!!
        
Warning:
Your entire traffic will be routed through the proxy, except if your threading mode is set to &apos;ffmpeg&apos;. There&apos;s no
guarantee for your IP not being exposed. If you live in a country where downloading Porn is a crime, please consider
using a VPN or Tor for a more safe approach. 

After submitting the proxy, Porn Fetch will do a short test if your IP is leaked by making a request to 
&apos;http://httpbin.org/ip&apos; with and without proxy to compare your IP address. 

All traffic will be sent with encryption, however, SSL won&apos;t be verified, meaning someone could break your encryption
and you won&apos;t get notified about it. Basically all SSL related errors will be completely ignored, but if your
proxy is good, SSL should work. 

Proxy implementation will be improved in the next release. All of it is currently in BETA. Please report any issues unless
they are related to the proxy itself e.g., closed connections and such things. You might want to higher the timeout
in Porn Fetch settings, because some proxies are just really slow

Please set your threading mode to &apos;Default&apos;. Most proxies can&apos;t handle what the threaded mode is capable of.
Seriously this thing can go up to 115 MB/s. Proxies can&apos;t handle that xD
If you want to see by yourself, use wireshark and monitor your network traffic.

DO NOT REPORT ANY ERRORS WHEN USING A PUBLIC PROXY!
They are just shit, and don&apos;t work well. If you come across connection errors with them it is by 99.9% the fault
of the proxy and not my fault ;)

If you still want to proceed, click O.K. Otherwise, close Porn Fetch now and restart it.</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../../../main.py" line="1695"/>
        <source>The model URL you entered seems to be invalid. Please check your input</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../../../main.py" line="1752"/>
        <source>Information: The Website {website} specified in the URL file isn&apos;t valid.</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../../../main.py" line="1782"/>
        <source>Couldn&apos;t determine which site you want to search on??? Please report this immediately!</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../../../main.py" line="1909"/>
        <source>
An error happened inside of Porn Fetch! 

{error}</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../../../main.py" line="2029"/>
        <source>Can&apos;t show thumbnail, due to your privacy settings ;)</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../../../main.py" line="2036"/>
        <source>No thumbnail available</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../../../main.py" line="2136"/>
        <source>Those credentials don&apos;t seem to be valid...</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../../../main.py" line="2142"/>
        <source>Login Successful!</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../../../main.py" line="2146"/>
        <source>Login Failed, please check your credentials and try again!</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../../../main.py" line="2149"/>
        <source>You are already logged in!</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../../../main.py" line="2161"/>
        <source>There&apos;s a problem with the login. Please make sure you login first and then you try to get videos based on your account.</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../../../main.py" line="2222"/>
        <location filename="../../../main.py" line="2234"/>
        <source>Invalid Category. Press &apos;list categories&apos; to see all possible ones.</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../../../main.py" line="2319"/>
        <source>
! Warning !
Some websites couldn&apos;t be accessed. Here&apos;s a detailed report:
------------------------------------------------------------
{formatted_results}</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../../../main.py" line="2352"/>
        <source>
FFmpeg isn&apos;t installed on your system... Some features won&apos;t be available:

- The FFmpeg threading mode
- Converting videos into a valid .mp4 format
- Writing tags / metadata into the videos

These features aren&apos;t necessary for Porn Fetch, but can be useful for some people.

To automatically install ffmpeg, just head over to the settings and press the magical button, or install ffmpeg in your
local PATH (e.g, through your linux package manager, or through the Windows PATH)

This warning won&apos;t be shown again.
                    </source>
        <translation type="unfinished"></translation>
    </message>
</context>
<context>
    <name>PornFetchRangeSelector</name>
    <message>
        <location filename="../form_range_selector.ui" line="14"/>
        <source>Video selector...</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_range_selector.ui" line="22"/>
        <source>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;meta charset=&quot;utf-8&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
hr { height: 1px; border-width: 0; }
li.unchecked::marker { content: &quot;\2610&quot;; }
li.checked::marker { content: &quot;\2612&quot;; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:&apos;Sans Serif&apos;; font-size:9pt; font-weight:400; font-style:normal;&quot;&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:&apos;Segoe UI&apos;;&quot;&gt;Select the range of videos to be automatically selected.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:&apos;Segoe UI&apos;;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:&apos;Segoe UI&apos;;&quot;&gt;For example, if you set the start to 5 and the end to 20, then all videos between 5-20 will be checked for downloading :)&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:&apos;Segoe UI&apos;;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:&apos;Segoe UI&apos;;&quot;&gt;Or select by a range in time:&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:&apos;Segoe UI&apos;;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:&apos;Segoe UI&apos;;&quot;&gt;For example if you want to download all videos in between 10 and 20 minutes do:&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:&apos;Segoe UI&apos;;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:&apos;Segoe UI&apos;;&quot;&gt;Start: 10&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:&apos;Segoe UI&apos;;&quot;&gt;End: 20&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:&apos;Segoe UI&apos;;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:&apos;Segoe UI&apos;;&quot;&gt;And click Apply.&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_range_selector.ui" line="47"/>
        <location filename="../form_range_selector.ui" line="92"/>
        <location filename="../form_range_selector.ui" line="113"/>
        <source>Apply</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_range_selector.ui" line="54"/>
        <source>Apply by time:</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_range_selector.ui" line="61"/>
        <location filename="../form_range_selector.ui" line="123"/>
        <source>0</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_range_selector.ui" line="68"/>
        <source>Enter the author&apos;s name</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_range_selector.ui" line="78"/>
        <source>Apply by Index:</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_range_selector.ui" line="85"/>
        <location filename="../form_range_selector.ui" line="99"/>
        <source>End:</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_range_selector.ui" line="106"/>
        <location filename="../form_range_selector.ui" line="130"/>
        <source>Start:</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_range_selector.ui" line="137"/>
        <source>Apply by author:</source>
        <translation type="unfinished"></translation>
    </message>
</context>
<context>
    <name>PornFetch_Desktop</name>
    <message>
        <location filename="../form_desktop.ui" line="26"/>
        <source>Porn Fetch V3.5 (C) Johannes Habel GPL 3</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="329"/>
        <source>Supported websites</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="461"/>
        <source>Download</source>
        <translation type="unfinished">Télecharger</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="480"/>
        <source>PornHub</source>
        <translation type="unfinished">PornHub</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="505"/>
        <source>Search for Videos. Select Website below</source>
        <translation type="unfinished">Chercher une vidéo : Sélectionner un site ci-dessous</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="524"/>
        <source>Playlist URL:</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="543"/>
        <source>Search Website</source>
        <translation type="unfinished">Chercher un site</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="562"/>
        <source>File:</source>
        <translation type="unfinished">Fichier :</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="581"/>
        <source>Model URL:</source>
        <translation type="unfinished">URL du model :</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="603"/>
        <source>Start</source>
        <translation type="unfinished">Démarrer</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="622"/>
        <source>HQPorner</source>
        <translation type="unfinished">HQPorner</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="641"/>
        <source>URL:</source>
        <translation type="unfinished">URL :</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="666"/>
        <source>URLs in the file must be separated with new lines!</source>
        <translation type="unfinished">Les URLS du fichier doivent être séparées par des lignes!</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="685"/>
        <source>XVideos</source>
        <translation type="unfinished">XVideos</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="710"/>
        <location filename="../form_desktop.ui" line="887"/>
        <location filename="../form_desktop.ui" line="1432"/>
        <location filename="../form_desktop.ui" line="1498"/>
        <location filename="../form_desktop.ui" line="1659"/>
        <location filename="../form_desktop.ui" line="1700"/>
        <source>Get Videos</source>
        <translation type="unfinished">Trouver les vidéos</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="729"/>
        <source>Enter a PornHub Playlist URL</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="748"/>
        <location filename="../form_desktop.ui" line="2072"/>
        <location filename="../form_desktop.ui" line="2115"/>
        <location filename="../form_desktop.ui" line="2161"/>
        <location filename="../form_desktop.ui" line="2204"/>
        <location filename="../form_desktop.ui" line="2247"/>
        <location filename="../form_desktop.ui" line="2316"/>
        <location filename="../form_desktop.ui" line="2473"/>
        <location filename="../form_desktop.ui" line="2500"/>
        <location filename="../form_desktop.ui" line="2620"/>
        <location filename="../form_desktop.ui" line="2634"/>
        <location filename="../form_desktop.ui" line="2689"/>
        <location filename="../form_desktop.ui" line="2753"/>
        <location filename="../form_desktop.ui" line="2791"/>
        <source>Help</source>
        <translation type="unfinished">Aide</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="767"/>
        <source>XNXX</source>
        <translation type="unfinished">XNXX</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="786"/>
        <source>Enter video URL</source>
        <translation type="unfinished">Entrer l&apos;URL de la vidéo</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="805"/>
        <source>Enter Model / Channel / Actress URL</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="824"/>
        <source>Search Query:</source>
        <translation type="unfinished">Recherche :</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="849"/>
        <source>Open File</source>
        <translation type="unfinished">Ouvrir</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="868"/>
        <source>EPorner</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="954"/>
        <source>Get Liked videos</source>
        <translation type="unfinished">Trouver les vidéos aimées</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="973"/>
        <source>Get watched videos</source>
        <translation type="unfinished">Trouver les vidées regardées</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="992"/>
        <source>E-Mail:</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="1011"/>
        <source>Login</source>
        <translation type="unfinished">Identifiant</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="1030"/>
        <source>Enter your PornHub E-Mail address (not your username, pornhub changed it) </source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="1049"/>
        <source>Get recommended videos</source>
        <translation type="unfinished">Trouver les recommendations</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="1068"/>
        <source>Password:</source>
        <translation type="unfinished">Mot de passe :</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="1090"/>
        <source>Enter your PornHub Password</source>
        <translation type="unfinished">Entrer le mot de passe PornHub</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="1356"/>
        <source>XNXX:</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="1192"/>
        <source>XVideos:</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="1205"/>
        <source>Eporner:</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="1247"/>
        <source>Info:</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="1179"/>
        <source>PornHub:</source>
        <translation type="unfinished">Pornhub :</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="1310"/>
        <source>HQPorner:</source>
        <translation type="unfinished">HQPorner :</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="1317"/>
        <source>MissAV</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="1363"/>
        <source>XHamster</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="1454"/>
        <source>Month</source>
        <translation type="unfinished">Mois</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="1476"/>
        <location filename="../form_desktop.ui" line="1561"/>
        <source>List of all categories</source>
        <translation type="unfinished">Liste des catégories</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="1520"/>
        <source>All Time</source>
        <translation type="unfinished">Toujours</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="1539"/>
        <location filename="../form_desktop.ui" line="1580"/>
        <source>Get videos by category</source>
        <translation type="unfinished">Trouver les vidéos par catégorie</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="1618"/>
        <source>Week</source>
        <translation type="unfinished">Semaine</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="1678"/>
        <source>Get random video</source>
        <translation type="unfinished">Prendre une vidée aléatoire</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="1719"/>
        <source>Get Brazzers videos</source>
        <translation type="unfinished">Trouver les vidéos Brazzers</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="1738"/>
        <source>Get Top Porn:</source>
        <translation type="unfinished">Récupérer les tendances Porn :</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="1760"/>
        <source>Get Video</source>
        <translation type="unfinished">Trouver la vidéo</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="1835"/>
        <source>Author</source>
        <translation type="unfinished">Auteur</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="1840"/>
        <source>Duration (minutes)</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="1852"/>
        <source>Do not clear videos</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="1865"/>
        <source>Automated selection tool</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="1875"/>
        <source>Show videos in reverse</source>
        <translation type="unfinished">Inverser l&apos;ordre des videos</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="1882"/>
        <source>Keyboard shortcuts</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="1901"/>
        <source>Does not stop downloading videos</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="1904"/>
        <source>Stop loading videos</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="1931"/>
        <source>Click on a video to show a thumbnail...</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="1971"/>
        <source>Download Selected Videos</source>
        <translation type="unfinished">Télecharger la sélection</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2029"/>
        <source>Performance</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2052"/>
        <source>Simultaneous downloads:</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2095"/>
        <source>Maximal workers:</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2138"/>
        <source>Maximal timeout:</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2184"/>
        <source>Maximal retries:</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2227"/>
        <source>Network delay (per Request, in seconds):</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2276"/>
        <source>Download Mode:</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2286"/>
        <source>High Performance</source>
        <translation type="unfinished">Performance haute</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2296"/>
        <source>FFMPEG</source>
        <translation type="unfinished">FFMPEG</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2306"/>
        <source>Default</source>
        <translation type="unfinished">Défaut</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2328"/>
        <source>Graphical User Interface</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2366"/>
        <source>System default</source>
        <translation type="unfinished">Langue système</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2379"/>
        <source>Graphical User Interface Language:</source>
        <translation type="unfinished">Language de l&apos;application :</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2389"/>
        <source>English</source>
        <translation type="unfinished">Anglais</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2399"/>
        <source>French</source>
        <translation type="unfinished">Français</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2409"/>
        <source>Chinese (simplified)</source>
        <translation type="unfinished">Chinois (simplifié)</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2419"/>
        <source>German</source>
        <translation type="unfinished">Allemand</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2426"/>
        <source>Enable custom font (Jetbrains Mono)</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2438"/>
        <source>System / Porn Fetch</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2486"/>
        <source>Startup:</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2493"/>
        <source>Download and Setup FFmpeg</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2507"/>
        <source>Internet checks</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2514"/>
        <source>Update checks</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2521"/>
        <source>Install Porn Fetch</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2534"/>
        <source>Privacy:</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2541"/>
        <source>Enable Anonymous mode</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2548"/>
        <source>Activate Proxy</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2562"/>
        <source>Videos</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2600"/>
        <source>Worst</source>
        <translation type="unfinished">Pas ouf</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2610"/>
        <source>Best</source>
        <translation type="unfinished">Meilleur</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2627"/>
        <source>Use directory system</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2641"/>
        <source>Output path:</source>
        <translation type="unfinished">Chemin de sortie :</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2648"/>
        <source>Do not convert</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2655"/>
        <source>Write metadata tags</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2662"/>
        <source>Model videos (PornHub)</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2672"/>
        <source>Open</source>
        <translation type="unfinished">Ouvrir</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2679"/>
        <source>Result Limit:</source>
        <translation type="unfinished">Limite de résultats :</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2696"/>
        <source>Use custom format:</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2709"/>
        <source>Quality:</source>
        <translation type="unfinished">Qualité :</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2716"/>
        <source>Both</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2723"/>
        <source>Featured videos</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2746"/>
        <source>Enter &quot;./&quot; for current directory</source>
        <translation type="unfinished">Entrer &quot;./&quot; pour utiliser le dossier courant</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2763"/>
        <source>Half</source>
        <translation type="unfinished">Moitié</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2770"/>
        <source>mp4</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2777"/>
        <source>User uploads</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2784"/>
        <source>Skip existing files</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2825"/>
        <source>Apply  (needs restart)</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2854"/>
        <source>Reset Porn Fetch to default settings</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2914"/>
        <source>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;meta charset=&quot;utf-8&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
hr { height: 1px; border-width: 0; }
li.unchecked::marker { content: &quot;\2610&quot;; }
li.checked::marker { content: &quot;\2612&quot;; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:&apos;Sans Serif&apos;; font-size:9pt; font-weight:400; font-style:normal;&quot;&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;Supported Websites:&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;Downloading:&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;- PornHub.com (supports total progress)&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;- HQPorner.com&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;- Eporner.com&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;- XNXX.com (supports total progress)&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;- XVideos.com (supports total progress)&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;- Missav.ws (and all of it&apos;s subsites, supports total progress)&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;- Xhamster.com&lt;br /&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;All sites support *threaded* downloads and selectable quality!&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;* hqporner and eporner running in QThreads, but they don&apos;t fetch segments. The video is directly&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;downloaded, therefore threading in a segment isn&apos;t needed.&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;Model / Channel Downloads&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;- PornHub.com&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;- HQPorner.com&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;- EPorner.com&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;- XNXX.com&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;- XVideos.com&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;Searching:&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;- PornHub.com&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;- HQPorner.com&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;- Xvideos.com&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;- Eporner.com&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;- XNXX.com&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;I am constantly working to support more websites.&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;If you want a specific site to be supported, just ask:&lt;br /&gt;&lt;br /&gt;Discord: echteralsfake&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;GitHub.com/echteralsfake/Porn_Fetch/issues&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;br /&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="2980"/>
        <source>Total:</source>
        <translation type="unfinished">Total :</translation>
    </message>
    <message>
        <location filename="../form_desktop.ui" line="3009"/>
        <source>Converting:</source>
        <translation type="unfinished"></translation>
    </message>
</context>
<context>
    <name>SetupInstallDialog</name>
    <message>
        <location filename="../form_install_dialog.ui" line="14"/>
        <source>Widget</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_install_dialog.ui" line="26"/>
        <source>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;meta charset=&quot;utf-8&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
hr { height: 1px; border-width: 0; }
li.unchecked::marker { content: &quot;\2610&quot;; }
li.checked::marker { content: &quot;\2612&quot;; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:&apos;Sans Serif&apos;; font-size:9pt; font-weight:400; font-style:normal;&quot;&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:&apos;Segoe UI&apos;; font-size:24pt; font-weight:700;&quot;&gt;Installation Mode&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:&apos;Segoe UI&apos;; font-size:16pt; text-decoration: underline; color:#0000ff;&quot;&gt;1) Inst&lt;/span&gt;&lt;span style=&quot; font-family:&apos;Segoe UI&apos;; font-size:14pt; text-decoration: underline; color:#0000ff;&quot;&gt;all&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:&apos;Segoe UI&apos;; font-size:12pt;&quot;&gt;This will install Porn Fetch into your system, meaning that you can run it directly from your Start Menu. e.g, press Windows key, type Porn Fetch and directly start it and on Linux it will be the same.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:&apos;Segoe UI&apos;; font-size:12pt;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:&apos;Segoe UI&apos;; font-size:12pt;&quot;&gt;Porn Fetch will be installed into the following path(s):&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:&apos;Segoe UI&apos;; font-size:12pt;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:&apos;Segoe UI&apos;; font-size:12pt;&quot;&gt;Windows: C:\Users\&amp;lt;user&amp;gt;\AppData\Local\pornfetch\&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:&apos;Segoe UI&apos;; font-size:12pt;&quot;&gt;Linux: ~/.local/share/pornfetch&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:&apos;Segoe UI&apos;;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:&apos;Segoe UI&apos;; font-size:16pt; text-decoration: underline; color:#00ff00;&quot;&gt;2) Portable&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:&apos;Segoe UI&apos;; font-size:12pt;&quot;&gt;This means, that Porn Fetch will not be installed and in order to use and start Porn Fetch you always need to double click on the file you have downloaded. This has some benefits as the uninstallation is easier and you have more control over it, but for the average user I do not recommend this.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:&apos;Segoe UI&apos;; font-size:12pt;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:&apos;Segoe UI&apos;; font-size:16pt; font-weight:700; color:#a100ff;&quot;&gt;Custom App name&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:&apos;Segoe UI&apos;; font-size:12pt; color:#ffffff;&quot;&gt;Down below you can enter  a custom name for Porn Fetch. You can then search with this name for Porn Fetch and Porn Fetch will not be found anymore when someone enters &amp;quot;Porn Fetch&amp;quot; on your PC. This can be useful if multiple persons use your PC and you don&apos;t want them to know you are using this application. It can also help if you are in public and people stare at your PC. Porn Fetch has also an option to fully hide, that it&apos;s a PornHub downloader.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:&apos;Segoe UI&apos;; font-size:12pt; color:#ffffff;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-size:12pt; color:#ffffff;&quot;&gt;If you leave it empty, Porn Fetch will remain as &amp;quot;Porn Fetch&amp;quot; in your short menu.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:&apos;Segoe UI&apos;; font-size:14pt; text-decoration: underline; color:#aa0000;&quot;&gt;NOTE:&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:&apos;Segoe UI&apos;; font-size:12pt;&quot;&gt;Installation was implemented in this release and might still be experimental. If you run into any issues, please report it on my GitHub. Thank you :&lt;/span&gt;&lt;span style=&quot; font-family:&apos;Segoe UI&apos;;&quot;&gt;) &lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:&apos;Segoe UI&apos;;&quot;&gt;&lt;br /&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_install_dialog.ui" line="61"/>
        <source>Custom App Name:</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_install_dialog.ui" line="71"/>
        <source>Enter your custom App Name here. Leave it empty to keep &quot;Porn Fetch&quot;</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_install_dialog.ui" line="82"/>
        <source>Install</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_install_dialog.ui" line="89"/>
        <source>Portable</source>
        <translation type="unfinished"></translation>
    </message>
</context>
<context>
    <name>SetupLicense</name>
    <message>
        <location filename="../form_license.ui" line="14"/>
        <source>Porn Fetch License Agreement (GPLv3)</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_license.ui" line="93"/>
        <source>Accept</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_license.ui" line="119"/>
        <source>Deny and Exit</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../form_license.ui" line="133"/>
        <source>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;meta charset=&quot;utf-8&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
hr { height: 1px; border-width: 0; }
li.unchecked::marker { content: &quot;\2610&quot;; }
li.checked::marker { content: &quot;\2612&quot;; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:&apos;JetBrainsMono Nerd Font Propo&apos;; font-size:11pt; font-weight:400; font-style:normal;&quot;&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-weight:700;&quot;&gt;GPL License Agreement for Porn Fetch&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;This program is free software: you may redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License or (at your option) any later version.&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;This program is distributed in the hope that it will be useful, but it is provided &lt;span style=&quot; font-weight:700;&quot;&gt;&amp;quot;AS IS&amp;quot; WITHOUT ANY WARRANTY&lt;/span&gt;; without even the implied warranties of &lt;span style=&quot; font-weight:700;&quot;&gt;MERCHANTABILITY&lt;/span&gt; or &lt;span style=&quot; font-weight:700;&quot;&gt;FITNESS FOR A PARTICULAR PURPOSE&lt;/span&gt;. For more details, see the GNU General Public License.&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;You should have received a copy of the GNU General Public License along with this program. If not, visit &lt;a href=&quot;https://www.gnu.org/licenses/&quot;&gt;&lt;span style=&quot; text-decoration: underline; color:#007af4;&quot;&gt;https://www.gnu.org/licenses/&lt;/span&gt;&lt;/a&gt;.&lt;/p&gt;
&lt;hr /&gt;
&lt;h2 style=&quot; margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-size:x-large; font-weight:700;&quot;&gt;Limitation of Liability&lt;/span&gt;&lt;/h2&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;Under no circumstances and under no legal theory—whether in tort, contract, or otherwise—shall the copyright holder or contributors be held liable for any direct, indirect, special, incidental, consequential, or exemplary damages of any kind. &lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;This includes, but is not limited to:&lt;/p&gt;
&lt;ul style=&quot;margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;&quot;&gt;
&lt;li style=&quot; margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;Damages for loss of goodwill &lt;/li&gt;
&lt;li style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;Work stoppage &lt;/li&gt;
&lt;li style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;Computer failure or malfunction &lt;/li&gt;
&lt;li style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;Loss of data &lt;/li&gt;
&lt;li style=&quot; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;Any other commercial damages or losses &lt;/li&gt;&lt;/ul&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;Even if such parties were informed of the possibility of such damages.&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;This limitation does not apply to liability for death or personal injury resulting from the negligence of such parties, where applicable law prohibits such a limitation. &lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-weight:700;&quot;&gt;Note:&lt;/span&gt; In some jurisdictions, the exclusion or limitation of incidental or consequential damages is not allowed. Therefore, these exclusions may not apply to you.&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;This Agreement constitutes the complete and exclusive understanding between the parties regarding the subject matter contained herein.&lt;/p&gt;
&lt;hr /&gt;
&lt;h2 style=&quot; margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-size:x-large; font-weight:700;&quot;&gt;Disclaimer&lt;/span&gt;&lt;/h2&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-weight:700;&quot;&gt;Porn Fetch&lt;/span&gt; violates the Terms of Service of all the websites it supports, including but not limited to:&lt;/p&gt;
&lt;ul style=&quot;margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;&quot;&gt;
&lt;li style=&quot; margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;a href=&quot;https://spankbang.com&quot;&gt;&lt;span style=&quot; text-decoration: underline; color:#007af4;&quot;&gt;spankbang.com&lt;/span&gt;&lt;/a&gt; &lt;/li&gt;
&lt;li style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;a href=&quot;https://pornhub.com&quot;&gt;&lt;span style=&quot; text-decoration: underline; color:#007af4;&quot;&gt;pornhub.com&lt;/span&gt;&lt;/a&gt; &lt;/li&gt;
&lt;li style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;a href=&quot;https://hqporner.com&quot;&gt;&lt;span style=&quot; text-decoration: underline; color:#007af4;&quot;&gt;hqporner.com&lt;/span&gt;&lt;/a&gt; &lt;/li&gt;
&lt;li style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;a href=&quot;https://eporner.com&quot;&gt;&lt;span style=&quot; text-decoration: underline; color:#007af4;&quot;&gt;eporner.com&lt;/span&gt;&lt;/a&gt; &lt;/li&gt;
&lt;li style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;a href=&quot;https://xnxx.com&quot;&gt;&lt;span style=&quot; text-decoration: underline; color:#007af4;&quot;&gt;xnxx.com&lt;/span&gt;&lt;/a&gt; &lt;/li&gt;
&lt;li style=&quot; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;a href=&quot;https://xvideos.com&quot;&gt;&lt;span style=&quot; text-decoration: underline; color:#007af4;&quot;&gt;xvideos.com&lt;/span&gt;&lt;/a&gt; &lt;/li&gt;&lt;/ul&gt;
&lt;h3 style=&quot; margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-size:large; font-weight:700;&quot;&gt;Usage Warning&lt;/span&gt;&lt;/h3&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;Using &lt;span style=&quot; font-weight:700;&quot;&gt;Porn Fetch&lt;/span&gt; may result in &lt;span style=&quot; font-weight:700;&quot;&gt;legal action&lt;/span&gt; being taken against you. The creator of this software is not liable for any damages or legal consequences resulting from its use.&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-weight:700;&quot;&gt;Porn Fetch&lt;/span&gt; was created solely for the purpose of enabling offline access to videos in scenarios where internet access is unavailable. &lt;/p&gt;
&lt;ul style=&quot;margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;&quot;&gt;
&lt;li style=&quot; margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;The redistribution of copyright-protected content obtained through Porn Fetch is &lt;span style=&quot; font-weight:700;&quot;&gt;strictly forbidden&lt;/span&gt;. &lt;/li&gt;
&lt;li style=&quot; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;Any misuse of this software to steal and redistribute copyrighted material is against its intended purpose and is not endorsed by the creator. &lt;/li&gt;&lt;/ul&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;The &lt;span style=&quot; font-weight:700;&quot;&gt;batch processing feature&lt;/span&gt; in Porn Fetch is intended to assist users without graphical user interfaces in downloading content for personal use, not for large-scale video theft or redistribution.&lt;/p&gt;
&lt;hr /&gt;
&lt;h2 style=&quot; margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-size:x-large; font-weight:700;&quot;&gt;Third-Party Software&lt;/span&gt;&lt;/h2&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-weight:700;&quot;&gt;Porn Fetch&lt;/span&gt; utilizes the following third-party tools and resources:&lt;/p&gt;
&lt;ol style=&quot;margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;&quot;&gt;
&lt;li style=&quot; margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-weight:700;&quot;&gt;FFmpeg&lt;/span&gt; &lt;/li&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;&quot;&gt;Used for video processing and conversion. &lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;&quot;&gt;FFmpeg is free software licensed under the GPL. &lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;&quot;&gt;For more information, visit &lt;a href=&quot;https://ffmpeg.org&quot;&gt;&lt;span style=&quot; text-decoration: underline; color:#007af4;&quot;&gt;https://ffmpeg.org&lt;/span&gt;&lt;/a&gt;.&lt;/p&gt;
&lt;li style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-weight:700;&quot;&gt;JetBrains Mono Font&lt;/span&gt; &lt;/li&gt;&lt;/ol&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;&quot;&gt;Copyright © 2019 JetBrains. All Rights Reserved. &lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;&quot;&gt;Licensed under the SIL Open Font License, Version 1.1. &lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;&quot;&gt;License details: &lt;a href=&quot;https://scripts.sil.org/OFL&quot;&gt;&lt;span style=&quot; text-decoration: underline; color:#007af4;&quot;&gt;https://scripts.sil.org/OFL&lt;/span&gt;&lt;/a&gt;.&lt;/p&gt;
&lt;hr /&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;Thank you for using &lt;span style=&quot; font-weight:700;&quot;&gt;Porn Fetch&lt;/span&gt; responsibly!&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation type="unfinished"></translation>
    </message>
</context>
<context>
    <name>main</name>
    <message>
        <location filename="../../../main.py" line="2506"/>
        <source>Done! Please restart.</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../../../main.py" line="2531"/>
        <source>No URLs in the current session...</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../../../main.py" line="2534"/>
        <source>FFmpeg has been installed. Please restart Porn Fetch :)</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../../../main.py" line="2557"/>
        <source>
            Information: A new version of Porn Fetch (v{__next_release__}) is out. I recommend you to update Porn Fetch. 
            Go to: https://github.com/EchterAlsFake/Porn_Fetch/releases/tag/ {__next_release__}

            Changelog:
            {markdown.markdown(changelog)}

            </source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../../backend/class_help.py" line="11"/>
        <source>
The result limit defines how many videos will be returned when performing a search or doing other operations which
involves loading multiple videos. This also affects models / channels and your liked videos. The result limit is
basically the number of videos which can be loaded into the tree widget (this thing where videos are displayed).
</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../../backend/class_help.py" line="24"/>
        <source>
You can set a delay between requests from you to PornHub. If you are downloading a lot of videos or experiencing 
&apos;client.call&apos; errors, you should enable a delay. By default the delay is turned off with the value 0

A good starting point is between 0.5 - 1.5

The longer the delay is, the longer it will take to download videos, load videos and generally do stuff.
This does NOT affect other sites!
</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../../backend/class_help.py" line="36"/>
        <source>
The maximal workers define the amount of maximal threads which can be started when using the threaded download mode.
One thread handles downloading one segment, so (in theory) 20 threads can download 20 segments at the same time.
This can of course be helpful when you have a very fast internet connection, but when you have a poor PC or running on
Android, you should set this to a lower value.

I recommend &apos;3&apos; for Android and 5 for low bandwidth connections &lt; 15000 bit/s
</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../../backend/class_help.py" line="44"/>
        <source>
The timeout handles the timeout for retrieving segments when using the threaded download mode. If you have a poor 
internet connection you can set this higher than 10. But this isn&apos;t required for most users!
</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../../backend/class_help.py" line="55"/>
        <source>
The Semaphore is a tool to limit the number of simultaneous actions / downloads.

For example: If the semaphore is set to 1, only 1 video will be downloaded at the same time.
If the semaphore is set to 4, 4 videos will be downloaded at the same time. Changing this is only useful, if
you have a really good internet connection and a good system.
</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../../backend/class_help.py" line="73"/>
        <source>
The different threading modes are used for different scenarios. 

1) High Performance:  Uses a class of workers to download multiple video segments at a time. Can be really fast if you
have a very strong internet connection. Maybe not great for low end systems.

2) FFMPEG:  ffmpeg is a tool for converting media files. ffmpeg will download every video segment and merge it directly
into the video file. This removes an extra step from the default method and is therefore a lot faster, but still not as 
good as high performance.

3) Default:  The default download mode will just download one video segment after the next one. If you get a lot of 
timeouts this can really slow down the process, as we need to wait for PornHub to return the video segments.
With the High Performance method, we can just download other segments while waiting which makes it so fast.
</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../../backend/class_help.py" line="84"/>
        <source>
The directory system will save videos in an intelligent way. If you download 3 videos form one Pornstar and 5 videos 
from another, Porn Fetch will automatically make folders for it and move the 3 videos into that one folder and the other
5 into the other. (This will still apply with your selected output path)

This can be helpful for organizing stuff, but is a more advanced feature, so the majority of users won&apos;t use it probably
</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../../backend/class_help.py" line="107"/>
        <source>
Create a .txt file and add URLs like this:

url1
url2
url3
...

Split them with new lines. No comma, not multiple URLs in the same line!
You can also add model URLs like this:

model#MODEL_URL

An example for a file would be:

https://de.pornhub.com/view_video.php?viewkey=ph5be76343323ff
https://de.pornhub.com/view_video.php?viewkey=ph5946e5f19585a
model#https://de.pornhub.com/pornstar/nancy-a
</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../../backend/class_help.py" line="115"/>
        <source>
The maximal retries defines how much attempts will be used for a network request. For example if an API calls
a URL for a website there will be &lt;AMOUNT&gt; of attempts until an error is thrown.
</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../../backend/class_help.py" line="143"/>
        <source>
User uploads and featured videos are two different things. User uploads are the videos which were really uploaded
by the model and the featured videos are videos the model is part or featured in.

For example the model Nancy Ace has like 10 self uploaded which she made by herself, but she is part in like thousands
of videos from other studios.

If you choose &quot;User Uploads&quot;, only self uploaded videos will be fetched, and the other way around :)</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../../backend/class_help.py" line="156"/>
        <source>
Metadata tags are saved inside of the file itself. These are tags that video players can read from and provide you information.
Some folder viewers also give you the ability to search files by specific metadata tags. Those tags can help organize and structure files.
Porn Fetch will by default save those tags inside of your video files. 

Tag writing is not supported for formats that are not mp4 files. Porn Fetch allows you to convert video files into other
formats, however, they use other standardization for metadata keys (a specifier), which is why I can&apos;t support other
video &apos;containers&apos;. 
</source>
        <translation type="unfinished"></translation>
    </message>
</context>
</TS>
