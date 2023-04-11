#!/usr/bin/env ruby
# RUBY_VERSION == 3.2

puts <<~'HEADER'
      ----------------------------
        ||     ||      ||     ||
        ||     ||      ||     ||
        ||  ___|| ____ ||___  ||
        || /   ||'    `||   \ ||
        ||____/||______||\____||
        ||\   \||      ||/   /||
        || `\  ||      ||  /' ||
        ||    `||\    /||'    ||
        ||     ||\ \/ /||     ||
        ||     || `\/' ||     ||
      ----------------------------
  jailed for crimes against parentheses

HEADER

printf '>>> '
STDOUT.flush
input = readline.chomp

# cant make this too easy
class Object
  def system(*)
    'nice try youre not getting the flag this way'
  end

  def spawn(*)
    'or this way either'
  end
end

if input =~ /[^a-z.;=_ ]/
  # be nice and print out what character failed
  puts "failure builds character: #{Regexp.last_match}"
  exit 1
end

eval(input)
