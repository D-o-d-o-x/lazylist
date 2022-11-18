Is it a list? Is it a generator? No its a
# LazyList

Have you ever found yourself in a situation, where you used a generator, but then realized, that you sometimes need an element from further in the future? Or specific past element? This very specific problem is no more, thank to LazyList! (Wow!)

## What does it do?
It's a list, that gets initialied using an iterable. The list uses the iterable to generate when new elements are accessed.
The LazyList is mutable and inserts, appends and extends are possible. The LazyList never contains holes, if you access at an index, all previous indexes that have not been generated will also be generated. You can use peak(1) to access the next element without incrementing the exposed iterable, peak(-3) looks 3 iterations into the past, peak(0) gives the current value...
