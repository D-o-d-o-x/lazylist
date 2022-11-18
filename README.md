Is it a list? Is it a generator? No its a
# LazyList

<p align='center'>
  <img src='./lazylist.svg'>
</p>

Have you ever found yourself in a situation, where you used a generator, but then realized, that you sometimes need an element from further in the future? Or specific past element? This very specific problem is no more, thank to LazyList! (Wow!)

## What does it do?
It's a list, that gets initialied using an iterable. The list uses the iterable to generate when new elements are accessed.
The LazyList is mutable and inserts, appends and extends are possible. The LazyList never contains holes, if you access at an index, all previous indexes that have not been generated will also be generated (append and extend will therefore let the generator run until it is empty). You can use peak(1) to access the next element without incrementing the exposed iterable, peak(-3) looks 3 iterations into the past, peak(0) gives the current value. lazyList[n] gives element at index/iteration n; lazyList[-1] return the last element (will run the generator until termination)  

When you try to access at an index, that the generator never generates, you get a StopIteration-Exception.
len(lazyList) will return inf, while the generator end has not been reached.

## Attribution

Icon is based on:

Lazy by Adrien Coquet from <a href="https://thenounproject.com/browse/icons/term/lazy/" target="_blank" title="Lazy Icons">Noun Project</a>

List by Kirby Wu from <a href="https://thenounproject.com/browse/icons/term/list/" target="_blank" title="List Icons">Noun Project</a>
