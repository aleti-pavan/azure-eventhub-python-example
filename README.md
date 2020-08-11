# azure-event-hub
Python Hello World example of Microsoft Azure Event Hub.

## Prerequisites

- Python 3.6.x
- _(Optional)_ [Virtual Environment Wrapper](https://python-guide-cn.readthedocs.io/en/latest/dev/virtualenvs.html)
- [Azure Event Hubs](https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-create) Setup


## Setup

### Mac/Linux

- `mkvirtualenv -p /usr/local/bin/python3 azure-event-hub`
- `workon python-azure-eventhub`
- `python setup.py develop`
- `pytest`
- Set Environment Variables in `.env`

### Windows

- `virtualenv <envname>`
- `.\<envname>\Scripts\activate.ps1 `
- `python setup.py develop`
- `pytest`
- Setup Envvironment Variables in `.env`

#### .env

[steps to get connection string]( https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-get-connection-string#get-connection-string-from-the-portal )

```
EVENT_HUB_CONNECTION_STRING=<Namespace_Connection_String> 
EVENT_HUB_TOPIC_HELLO_WORLD_NAME=<eventhub-name>
EVENT_HUB_TOPIC_HELLO_WORLD_PARTITION=0
```

## Run

#### Send Message
`python spike-send.py <message>`

`bash: for i in {1..100}; do python spike-send.py "Message $i"; done `

`Powershell: for($i=0; $i -le 20; $i++) {python .\spike-send.py "Message $i"}`


#### Receive Messages
`python spike-receive.py`

## Example Output
```
➜ python spike-send.py
2020-08-11 15:01:29,901 - Send - INFO - Sending message: Message 4
2020-08-11 15:01:30,291 - Send - INFO - Runtime: 0.03300976753234863 seconds
➜ python spike-receive.py

2020-08-11 15:03:57,431 - Receive - INFO - Received:<azure.eventhub.common.Offset object at 0x000002E5492ED518>|47-Message:Message 4
```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-work`
3. Commit your changes: `git commit -am 'Add some work'`
4. Push to the branch: `git push origin my-work`
5. Submit a pull request :D
