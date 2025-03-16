
import boto3


def create_input_security_group(cidr):
    try:
        ml = boto3.client('medialive')
        group = ml.create_input_security_group(
            Tags={
                'test': 'apmc'
            },
            WhitelistRules=[
                {
                    'Cidr': cidr
                },
            ]
        )
        print(f'Created security group: \n${group}')
        return group['SecurityGroup']['Id']
    except Exception as err:
        print(f'Error: ${err}')
        return None
    


def create_rtmp_input(name, sources, destinations, security_groups):
    try: 
        ml = boto3.client('medialive')
        input = ml.create_input(
            Name=name,
            Sources=sources,
            Destinations=destinations,
            InputSecurityGroups=security_groups,
            Tags={
                'test': 'apmc'
            },
            Type='RTMP_PUSH',
            InputNetworkLocation='AWS',
        )
        print(f'Created RTMP (Push) input: \n${input}')
        return input
    except Exception as err:
        print(f'Error: ${err}')
        return None


def main():
    name = 'ExampleInput'

    sources = []

    destinations = [
        {
            'StreamName': 'ExampleStream',
        },
    ]

    # A valid security group ID is required so create a placeholder 
    test_group = create_input_security_group('10.0.0.0/8')
    security_groups = [
        test_group
    ]

    create_rtmp_input(name, sources, destinations, security_groups)


if __name__ == "__main__":
    main()
