#!/usr/bin/env ruby
puts ARGV[0].scan(/^h(?!bon)(b[nt]{1,6})$/).join
