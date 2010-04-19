<?xml version='1.0'?>

<!-- This is a Docbook XSLT Customization Layer. Your XSLT processor will use this file instead of the default Docbook stylesheet.
     This file includes the original stylesheet, and then allows you to override the defaults with your own values. 
     Examples are in this file.
-->

<xsl:stylesheet 
   xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0"
   xmlns:fo="http://www.w3.org/1999/XSL/Format"
   xmlns:xslthl="http://xslthl.sf.net"
   xmlns:d="http://docbook.org/ns/docbook"
   xmlns:saxon="http://icl.com/saxon"
   extension-element-prefixes="saxon"
>
  <xsl:import href="html_base.xml" />

  <xsl:output method="html"
              encoding="UTF-8"
              indent="no"
              saxon:character-representation="native;decimal"/>

  <!-- graphics for the alerts, tips, cautions, warnings, notes, etc. Build your own or turn this off! -->
  <xsl:param name="admon.graphics" select="1" />
  <xsl:param name="html.stylesheet" select="'style.css'" />
  <xsl:param name="use.extensions" select="1"/>
  <xsl:param name="linenumbering.extension" select="1"/>
  <xsl:param name="linenumbering.everyNth" select="1"/>
  <xsl:param name="linenumbering.separator"><xsl:text>| </xsl:text></xsl:param>
  <xsl:param name="highlight.source" select="1" />

</xsl:stylesheet>