#!/usr/bin/env ruby

#  e.g. rake pdf                 # Create a PDF
#       rake xhtml               # Create an XHTML file
#       rake chm                 # Create a CHM help file
#       rake pdf VALIDATE=false  # skips validation


#=================== Set path to DOCBOOK files =======

temp_root = ENV['SHORT_ATTENTION_SPAN_DOCBOOK_PATH'] || "/Users/brianhogan/docbook"
# fix for windows paths with double-quotes and bad slashes.
DOCBOOK_ROOT = temp_root.gsub("\\", "/").gsub('"', "")
require "#{DOCBOOK_ROOT}/make"
