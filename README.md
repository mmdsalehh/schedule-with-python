# How to use

#### First import the require libraries

```
from schedule import Schedule
from datetime import datetime, timedelta
```

#### Then make an object from schedule class like this

`schedule = Schedule()`

#### Use 'add' method to add command:

```
schedule.add({
    'type': 'command',
    'command': ['ls'],
    'time': datetime.now() + timedelta(seconds=2),
})
```

#### To add reminder

```
schedule.add({
    'type': 'reminder',
    'reminder_text': 'The example of reminder text',
    'time': datetime.now() + timedelta(seconds=5),
})
```
#### Then:

`schedule.run()`
