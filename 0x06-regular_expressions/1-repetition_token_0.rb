#!/usr/bin/env ruby
# regular expression that matches given cases

puts ARGV[0].scan(/hbt{2,5}n/).join
