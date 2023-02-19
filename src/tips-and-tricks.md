# Tips & Tricks

## XML

`labwc` parses XML in an element/attribute agnostic way. This is a design
decision to increase config file flexibility and keep code simple. In practical
terms, this means that `<a><b>c</b></a>` is equivalent to `<a b="c" />`.

The following three are therefore treated the same:

```
<action>
	<name>Execute</name>
	<command>foot</command>
</action>
```

```
<action name="Execute">
	<command>foot</command>
</action>
```

```
<action name="Execute" command="foot" />
```

The benefit of the final one is brevity whereas the advantage of the first two
is that you can add ' and " within the `<command>` block, for example:

```
<command>sh -c 'grim -g "`slurp`"'</command>
```

