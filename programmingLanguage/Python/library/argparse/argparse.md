
# argparse

# · create parser


```python
import argparse
```


```python
parser = argparse.ArgumentParser()
```

> When parser.parse_args is called optional args will be identified by the prefix, the remain args will be assumed to be positional
> Positional args are required by default.


```python
parser.add_argument('-f', '--foe')
parser.add_argument('bar')
parser.print_help()
```

    usage: ipykernel_launcher.py [-h] [-f FOE] bar
    
    positional arguments:
      bar
    
    optional arguments:
      -h, --help         show this help message and exit
      -f FOE, --foe FOE


## · add_argument

### · action

* 'store'

> default action. Just store the value


```python
parser.parse_args('-f abc bar'.split())
```




    Namespace(bar='bar', foe='abc')




```python
parser.parse_args('-f 123 bar'.split())
```




    Namespace(bar='bar', foe='123')



* 'store_const'

> This stores the value specified by the const keyword arg.


```python
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--foo', action='store_const', const=42)
```




    _StoreConstAction(option_strings=['-f', '--foo'], dest='foo', nargs=0, const=42, default=None, type=None, choices=None, help=None, metavar=None)




```python
parser.parse_args(['--foo'])
```




    Namespace(foo=42)



> 'store_const' is used as flag, so it doesn't accept the user defined value, it can be only choosed or not choosed.


```python
parser.parse_args('--foo abc'.split())
```

    usage: ipykernel_launcher.py [-h] [-f]
    ipykernel_launcher.py: error: unrecognized arguments: abc



    An exception has occurred, use %tb to see the full traceback.


    SystemExit: 2



    /usr/local/lib/python2.7/site-packages/IPython/core/interactiveshell.py:2886: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.
      warn("To exit: use 'exit', 'quit', or Ctrl-D.", stacklevel=1)


* 'store_true' or 'store_false'

> special case of 'store_const' used for storing the values True and False


```python
parser = argparse.ArgumentParser()
parser.add_argument('-t', action='store_true')
parser.add_argument('-w', action='store_false')

parser.parse_args(['-t'])
```




    Namespace(t=True, w=True)




```python
parser.parse_args(['-w'])
```




    Namespace(t=False, w=False)



* 'append'

> This stores a list.

* 'append_const'

> stores a list, the list name specified by the dest arg


```python
parser = argparse.ArgumentParser()
parser.add_argument('--list', action='append')

parser.add_argument('--list-const1', dest='list', action='append_const', const=1)
parser.add_argument('--list-const2', dest='list', action='append_const', const=21)
```




    _AppendConstAction(option_strings=['--list-const2'], dest='list', nargs=0, const=21, default=None, type=None, choices=None, help=None, metavar=None)




```python
parser.parse_args('--list 1 --list 2'.split())
```




    Namespace(list=['1', '2'])




```python
parser.parse_args('--list 1 --list 2 --list-const1 --list-const2'.split())
```




    Namespace(list=['1', '2', 1, 21])



> nargs associates a different number of command-line arguments with a single action
> N is an integer


```python
parser = argparse.ArgumentParser()
parser.add_argument('--foo', nargs=10)
parser.add_argument('-c')
parser.add_argument('bar', nargs=1)
parser.parse_args('c --foo a b d -c c'.split())
```

    usage: ipykernel_launcher.py [-h]
                                 [--foo FOO FOO FOO FOO FOO FOO FOO FOO FOO FOO]
                                 [-c C]
                                 bar
    ipykernel_launcher.py: error: argument --foo: expected 10 argument(s)



    An exception has occurred, use %tb to see the full traceback.


    SystemExit: 2



> '?' refer to 0 or 1


```python
parser = argparse.ArgumentParser()
parser.add_argument('--foo', nargs='?', const='c', default='d')
parser.add_argument('bar', nargs='?')
parser.parse_args(['XX', '--foo', 'YY'])
```




    Namespace(bar='XX', foo='YY')




```python
parser.parse_args(['XX', '--foo'])
```




    Namespace(bar='XX', foo='c')




```python
parser.parse_args(['XX'])
```




    Namespace(bar='XX', foo='d')




```python
parser = argparse.ArgumentParser()
parser.add_argument('--foo', nargs='?', default='d')
parser.add_argument('bar', nargs='?')
parser.parse_args(['XX', '--foo'])
```




    Namespace(bar='XX', foo=None)




```python
parser.parse_args(['XX'])
```




    Namespace(bar='XX', foo='d')




```python
parser = argparse.ArgumentParser()
parser.add_argument('--foo', nargs='?')
parser.add_argument('bar', nargs='?')
parser.parse_args(['XX'])
```




    Namespace(bar='XX', foo=None)



> '*' refer to 0-inf


```python
parser = argparse.ArgumentParser()
parser.add_argument('--foo', nargs='*')
parser.parse_args(['--foo'])
```




    Namespace(foo=[])




```python
parser = argparse.ArgumentParser()
parser.add_argument('--foo', nargs='*', const='c')
parser.parse_args(['--foo'])
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-22-8f6081770009> in <module>()
          1 parser = argparse.ArgumentParser()
    ----> 2 parser.add_argument('--foo', nargs='*', const='c')
          3 parser.parse_args(['--foo'])


    /usr/local/Cellar/python@2/2.7.15_1/Frameworks/Python.framework/Versions/2.7/lib/python2.7/argparse.pyc in add_argument(self, *args, **kwargs)
       1292         if not _callable(action_class):
       1293             raise ValueError('unknown action "%s"' % (action_class,))
    -> 1294         action = action_class(**kwargs)
       1295 
       1296         # raise an error if the action type is not callable


    /usr/local/Cellar/python@2/2.7.15_1/Frameworks/Python.framework/Versions/2.7/lib/python2.7/argparse.pyc in __init__(self, option_strings, dest, nargs, const, default, type, choices, required, help, metavar)
        821                              'true or store const may be more appropriate')
        822         if const is not None and nargs != OPTIONAL:
    --> 823             raise ValueError('nargs must be %r to supply const' % OPTIONAL)
        824         super(_StoreAction, self).__init__(
        825             option_strings=option_strings,


    ValueError: nargs must be '?' to supply const



```python
parser = argparse.ArgumentParser()
parser.add_argument('--foo', nargs='*', default='c')
parser.parse_args(['--foo'])
```




    Namespace(foo=[])




```python
parser.parse_args([])
```




    Namespace(foo='c')



> '+' refer to at least one


```python
parser = argparse.ArgumentParser()
parser.add_argument('--foo', nargs='+')
parser.parse_args(['--foo', 'XX', 'YY'])
```




    Namespace(foo=['XX', 'YY'])




```python
parser.parse_args(['--foo'])
```

    usage: ipykernel_launcher.py [-h] [--foo FOO [FOO ...]]
    ipykernel_launcher.py: error: argument --foo: expected at least one argument



    An exception has occurred, use %tb to see the full traceback.


    SystemExit: 2



> argparse.REMAINDER gather the remaining args into a list

> The args after the positional arg are considered as remaining args


```python
parser = argparse.ArgumentParser()
parser.add_argument('bar')
parser.add_argument('--foo')
parser.add_argument('args', nargs=argparse.REMAINDER)
parser.parse_args(['bar', '--foo', 'f', 'arg', '--args', 'xx', 'yy', 'zz'])
```




    Namespace(args=['--foo', 'f', 'arg', '--args', 'xx', 'yy', 'zz'], bar='bar', foo=None)




```python
parser.parse_args(['--foo', 'f', 'b', 'arg', '--args', 'xx', 'yy', 'zz'])
```




    Namespace(args=['arg', '--args', 'xx', 'yy', 'zz'], bar='b', foo='f')



* type

> for type-checking<br/>
> common built-in types and funcitons canbe used directly as the value of the type arg


```python
parser = argparse.ArgumentParser()
parser.add_argument('--foo', type=int)
parser.add_argument('--bar', type=argparse.FileType('w'))
parser.add_argument('--open', type=open)
args = parser.parse_args('--foo 2 --bar temp.txt'.split())
print('args=%r' % args)
args.bar.writelines("abcde")
args.bar.close()
args = parser.parse_args('--foo 2 --open temp.txt'.split())
print('args=%r' % args)
print(args.open.readlines())
args.open.close()
import os
os.remove('temp.txt')
```

    args=Namespace(bar=<open file 'temp.txt', mode 'w' at 0x1095fdae0>, foo=2, open=None)
    args=Namespace(bar=None, foo=2, open=<open file 'temp.txt', mode 'r' at 0x1095f7f60>)
    ['abcde']

