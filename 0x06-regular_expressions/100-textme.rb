#!/usr/bin/env ruby
log_entry = ARGV[0]
sender_match = log_entry.match(/from:(.*?)\]/)
receiver_match = log_entry.match(/to:(.*?)\]/)
flags_match = log_entry.match(/flags:(.*?)\]/)

sender = sender_match ? sender_match[1] : ""
receiver = receiver_match ? receiver_match[1] : ""
flags = flags_match ? flags_match[1] : ""
puts "#{sender},#{receiver},#{flags}"