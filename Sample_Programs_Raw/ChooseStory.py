#coding=<utf-8>

part_one = """
Two roads diverged in a yellow wood,
And sorry I could not travel both
And be one traveller, long I stood
And looked down one as far as I could
To where it bent in the undergrowth;
"""

part_firstroad = """
\n
Then took the other, as just as fair,
And having perhaps the better claim,
Because it was grassy and wanted wear;
Though as for that the passing there
Had worn them really about the same,

And both that morning equally lay
In leaves no step had trodden black.
Oh, I kept the first for another day!
Yet knowing how way leads on to way,
I doubted if I should ever come back.

I shall be telling this with a sigh
Somewhere ages and ages hence:
Two roads diverged in a wood, and I-
I took the one less traveled by,
And that has made all the difference.
\n
"""

part_secondroad = """\n
Then took the other, just as fair,
And having perhaps the better claim,
Because it was worn and proven,
I kept my shoes in good mien,

And so they took me long and far,
to nations and places across the world
Sheltered by trees or Terra's star,
So without regret I went my way,
I opened my mind like a flag unfurled.

I shall be telling this with a cry
somewhere ages and ages neigh:
Two roads diverged in a wood, and I-
I took the one most travelled by,
And that has made all the difference.
\n
"""

print part_one
print "\n\nWhat would you like to do next?"
print "\n1) Take first road."
print "\n2) Take the second road."

choice = raw_input("\n>>>? ")

try:
	int(choice)
	
	if 1 > choice > 2:
		raise IOError
	
except:
	print "Please select an integer either 1 or 2"

if choice == '1':
	print part_firstroad
		
elif choice == '2':
	print part_secondroad

 





















