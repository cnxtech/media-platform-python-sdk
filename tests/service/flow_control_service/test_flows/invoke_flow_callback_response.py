invoke_flow_callback_response = {
    'invocation': {
        'sources': [],
        'entryPoints': ['import1'],
        'notification': None
    },
    'operations': {
        'import1': {
            'status': 'success',
            'deleteSources': False,
            'jobs': ['g_1'],
            'specification': {
                'destination': {
                    'directory': None,
                    'path': '/imports/video.mp4',
                    'acl': 'public',
                    'lifecycle': None
                },
                'sourceUrl': 'https://fish.com/dag.gadol'
            },
            'results': [
                {
                    'mimeType': 'video/mp4',
                    'hash': None,
                    'urn': 'urn:file:123',
                    'dateCreated': '2018-01-11T13:15:57Z',
                    'path': '/imports/video.mp4',
                    'dateUpdated': '2018-01-11T13:15:57Z',
                    'acl': 'public',
                    'type': '-',
                    'id': 'abcd',
                    'size': 4151438,
                    'lifecycle': None
                }
            ],
            'extraResults': {},
            'sources': [],
            'successors': ['callback1'],
            'type': 'file.import'
        },
        'callback1': {
            'status': 'success',
            'deleteSource': False,
            'specification': {
                'url': 'http://requestbin.fullcontact.com/sc9kxnsc',
                'attachment': {'attachment-key': 'attachment-value'},
                'headers': {'header': 'value'},
                'type': 'flow.callback',
                'passthrough': False,
            },
            'results': [],
            'extraResults': {},
            'sources': [],
            'successors': [],
            'type': 'flow.callback'
        }
    },
    'id': '12342134',
    'status': 'success',
    'error': None,

}