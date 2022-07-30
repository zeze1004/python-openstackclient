.. _command-structure:

=================
Command Structure
=================

OpenStackClient has a consistent and predictable format for all of its commands.

Commands take the form::

    openstack [<global-options>] <object-1> <action> [<object-2>] [<command-arguments>]

.. NOTE::

  All long options names begin with two dashes (``--``) and use a single dash
  (``-``) internally between words (``--like-this``).  Underscores (``_``) are
  not used in option names.

Global Options
--------------

Global options are global in the sense that they apply to every command
invocation regardless of action to be performed. They include authentication
credentials and API version selection. Most global options have a corresponding
environment variable that may also be used to set the value. If both are
present, the command-line option takes priority. The environment variable
names are derived from the option name by dropping the leading dashes (``--``),
converting each embedded dash (``-``) to an underscore (``_``), and converting
to upper case.

For example, the default value of ``--os-username`` can be set by defining
the environment variable ``OS_USERNAME``.


Command Object(s) and Action
----------------------------

Commands consist of an object described by one or more words followed by
an action.  Commands that require two objects have the primary object ahead
of the action and the secondary object after the action. Any positional
arguments identifying the objects shall appear in the same order as the
objects.  In badly formed English it is expressed as "(Take) object1
(and perform) action (using) object2 (to it)."

::

    <object-1> <action> <object-2>

Examples:

.. code-block:: bash

    $ group add user <group> <user>

    $ volume type list   # 'volume type' is a two-word single object


Command Arguments and Options
-----------------------------

Each command may have its own set of options distinct from the global options.
They follow the same style as the global options and always appear between
the command and any positional arguments the command requires.


Objects
-------

The objects consist of one or more words to compose a unique name.
Occasionally when multiple APIs have a common name with common
overlapping purposes there will be options to select which object to use, or
the API resources will be merged, as in the ``quota`` object that has options
referring to both Compute and Volume quotas.

* ``access token``: (**Identity**) long-lived OAuth-based token
* ``address scope``: (**Network**) a scope of IPv4 or IPv6 addresses
* ``aggregate``: (**Compute**) a grouping of compute hosts
* ``availability zone``: (**Compute**, **Network**, **Volume**) a logical partition of hosts or block storage or network services
* ``block storage cluster``: (**Volume**) clusters of volume services
* ``block storage resource filter``: (**Volume**) filters for volume service resources
* ``catalog``: (**Identity**) service catalog
* ``command``: (**Internal**) installed commands in the OSC process
* ``compute agent``: (**Compute**) a cloud Compute agent available to a hypervisor
* ``compute service``: (**Compute**) a cloud Compute process running on a host
* ``configuration``: (**Internal**) OpenStack client configuration
* ``consistency group``: (**Volume**) a consistency group of volumes
* ``consistency group snapshot``: (**Volume**) a point-in-time copy of a consistency group
* ``console log``: (**Compute**) server console text dump
* ``console url``: (**Compute**) server remote console URL
* ``consumer``: (**Identity**) OAuth-based delegatee
* ``container``: (**Object Storage**) a grouping of objects
* ``credential``: (**Identity**) specific to identity providers
* ``domain``: (**Identity**) a grouping of projects
* ``ec2 credentials``: (**Identity**) AWS EC2-compatible credentials
* ``endpoint``: (**Identity**) the base URL used to contact a specific service
* ``endpoint group``: (**Identity**) group endpoints to be used as filters
* ``extension``: (**Compute**, **Identity**, **Network**, **Volume**) OpenStack server API extensions
* ``federation protocol``: (**Identity**) the underlying protocol used while federating identities
* ``flavor``: (**Compute**) predefined server configurations: ram, root disk and so on
* ``fixed ip``: (**Compute**) - an internal IP address assigned to a server
* ``floating ip``: (**Network**) - a public IP address that can be mapped to a server
* ``floating ip pool``: (**Network**) - a pool of public IP addresses
* ``group``: (**Identity**) a grouping of users
* ``host``: (**Compute**) - the physical computer running compute services
* ``hypervisor``: (**Compute**) the virtual machine manager
* ``hypervisor stats``: (**Compute**) hypervisor statistics over all compute nodes
* ``identity provider``: (**Identity**) a source of users and authentication
* ``image``: (**Image**) a disk image
* ``image member``: (**Image**) a project that is a member of an Image
* ``ip availability``: (**Network**) - details of IP usage of a network
* ``keypair``: (**Compute**) an SSH public key
* ``limits``: (**Compute**, **Volume**) resource usage limits
* ``mapping``: (**Identity**) a definition to translate identity provider attributes to Identity concepts
* ``module``: (**Internal**) - installed Python modules in the OSC process
* ``network``: (**Compute**, **Network**) - a virtual network for connecting servers and other resources
* ``network agent``: (**Network**) - A network agent is an agent that handles various tasks used to implement virtual networks
* ``network auto allocated topology``: (**Network**) - an auto-allocated topology for a project
* ``network flavor``: (**Network**) - allows the user to choose the type of service by a set of advertised service capabilities (e.g., LOADBALANCER, FWAAS, L3, VPN, etc) rather than by a provider type or named vendor
* ``network flavor profile``: (**Network**) - predefined neutron service configurations: driver
* ``network meter``: (**Network**) - allow traffic metering in a network
* ``network meter rule``: (**Network**) - rules for network traffic metering
* ``network rbac``: (**Network**) - an RBAC policy for network resources
* ``network qos rule``: (**Network**) - a QoS rule for network resources
* ``network qos policy``: (**Network**) - a QoS policy for network resources
* ``network qos rule type``: (**Network**) - list of QoS available rule types
* ``network segment``: (**Network**) - a segment of a virtual network
* ``network segment range``: (**Network**) - a segment range for tenant network segment allocation
* ``network service provider``: (**Network**) - a driver providing a network service
* ``object``: (**Object Storage**) a single file in the Object Storage
* ``object store account``: (**Object Storage**) owns a group of Object Storage resources
* ``policy``: (**Identity**) determines authorization
* ``port``: (**Network**) - a virtual port for connecting servers and other resources to a network
* ``project``: (**Identity**) owns a group of resources
* ``quota``: (**Compute**, **Volume**) resource usage restrictions
* ``region``: (**Identity**) a subset of an OpenStack deployment
* ``request token``: (**Identity**) temporary OAuth-based token
* ``role``: (**Identity**) a policy object used to determine authorization
* ``role assignment``: (**Identity**) a relationship between roles, users or groups, and domains or projects
* ``router``: (**Network**) - a virtual router
* ``security group``: (**Compute**, **Network**) - groups of network access rules
* ``security group rule``: (**Compute**, **Network**) - the individual rules that define protocol/IP/port access
* ``server``: (**Compute**) virtual machine instance
* ``server backup``: (**Compute**) backup server disk image by using snapshot method
* ``server dump``: (**Compute**) a dump file of a server created by features like kdump
* ``server event``: (**Compute**) events of a server
* ``server group``: (**Compute**) a grouping of servers
* ``server image``: (**Compute**) saved server disk image
* ``service``: (**Identity**) a cloud service
* ``service provider``: (**Identity**) a resource that consumes assertions from an ``identity provider``
* ``subnet``: (**Network**) - a contiguous range of IP addresses assigned to a network
* ``subnet pool``: (**Network**) - a pool of subnets
* ``token``: (**Identity**) a bearer token managed by Identity service
* ``trust``: (**Identity**) project-specific role delegation between users, with optional impersonation
* ``usage``: (**Compute**) display host resources being consumed
* ``user``: (**Identity**) individual cloud resources users
* ``user role``: (**Identity**) roles assigned to a user
* ``volume``: (**Volume**) block volumes
* ``volume attachment``: (**Volume**) an attachment of a volumes to a server
* ``volume backup``: (**Volume**) backup for volumes
* ``volume backend capability``: (**Volume**) volume backend storage capabilities
* ``volume backend pool``: (**Volume**) volume backend storage pools
* ``volume backup record``: (**Volume**) volume record that can be imported or exported
* ``volume backend``: (**Volume**) volume backend storage
* ``volume group``: (**Volume**) group of volumes
* ``volume group snapshot``: (**Volume**) a point-in-time copy of a volume group
* ``volume group type``: (**Volume**) deployment-specific types of volumes groups available
* ``volume host``: (**Volume**) the physical computer for volumes
* ``volume message``: (**Volume**) volume API internal messages detailing volume failure messages
* ``volume qos``: (**Volume**) quality-of-service (QoS) specification for volumes
* ``volume snapshot``: (**Volume**) a point-in-time copy of a volume
* ``volume type``: (**Volume**) deployment-specific types of volumes available
* ``volume service``: (**Volume**) services to manage block storage operations
* ``volume transfer request``: (**Volume**) volume owner transfer request

Plugin Objects
--------------

The following are known `Objects` used by OpenStack
:ref:`plugins`. These are listed here to avoid name
conflicts when creating new plugins. For a complete list check out
:ref:`plugin-commands`.

* ``acl``: (**Key Manager (Barbican)**)
* ``acl user``: (**Key Manager (Barbican)**)
* ``action definition``: (**Workflow Engine (Mistral)**)
* ``action execution``: (**Workflow Engine (Mistral)**)
* ``appcontainer``: (**Application Container (Zun)**)
* ``appcontainer host``: (**Application Container (Zun)**)
* ``appcontainer image``: (**Application Container (Zun)**)
* ``appcontainer network``: (**Application Container (Zun)**)
* ``appcontainer service``: (**Application Container (Zun)**)
* ``baremetal``: (**Baremetal (Ironic)**)
* ``claim``: (**Messaging (Zaqar)**)
* ``cluster``: (**Clustering (Senlin)**)
* ``cluster action``: (**Clustering (Senlin)**)
* ``cluster event``: (**Clustering (Senlin)**)
* ``cluster members``: (**Clustering (Senlin)**)
* ``cluster node``: (**Clustering (Senlin)**)
* ``cluster policy``: (**Clustering (Senlin)**)
* ``cluster policy binding``: (**Clustering (Senlin)**)
* ``cluster policy type``: (**Clustering (Senlin)**)
* ``cluster profile``: (**Clustering (Senlin)**)
* ``cluster profile type``: (**Clustering (Senlin)**)
* ``cluster receiver``: (**Clustering (Senlin)**)
* ``cron trigger``: (**Workflow Engine (Mistral)**)
* ``database flavor``: (**Database (Trove)**)
* ``dataprocessing data source``: (**Data Processing (Sahara)**)
* ``dataprocessing image``: (**Data Processing (Sahara)**)
* ``dataprocessing image tags``: (**Data Processing (Sahara)**)
* ``dataprocessing plugin``: (**Data Processing (Sahara)**)
* ``loadbalancer``: (**Load Balancer (Octavia)**)
* ``loadbalancer healthmonitor``: (**Load Balancer (Octavia)**)
* ``loadbalancer l7policy``: (**Load Balancer (Octavia)**)
* ``loadbalancer l7rule``: (**Load Balancer (Octavia)**)
* ``loadbalancer listener``: (**Load Balancer (Octavia)**)
* ``loadbalancer member``: (**Load Balancer (Octavia)**)
* ``loadbalancer pool``: (**Load Balancer (Octavia)**)
* ``message-broker cluster``: (**Message Broker (Cue)**)
* ``messaging``: (**Messaging (Zaqar)**)
* ``messaging flavor``: (**Messaging (Zaqar)**)
* ``network subport``: (**Networking (Neutron)**)
* ``network trunk``: (**Networking (Neutron)**)
* ``orchestration resource``: (**Orchestration (Heat)**)
* ``orchestration template``: (**Orchestration (Heat)**)
* ``pool``: (**Messaging (Zaqar)**)
* ``ptr record``: (**DNS (Designate)**)
* ``queue``: (**Messaging (Zaqar)**)
* ``recordset``: (**DNS (Designate)**)
* ``rsd``: (**Disaggregated Hardware Resource Management (RSD)**)
* ``search`` (**Search (Searchlight)**)
* ``search facet`` (**Search (Searchlight)**)
* ``search resource type`` (**Search (Searchlight)**)
* ``secret``: (**Key Manager (Barbican)**)
* ``secret container``: (**Key Manager (Barbican)**)
* ``secret order``: (**Key Manager (Barbican)**)
* ``software config``: (**Orchestration (Heat)**)
* ``software deployment``: (**Orchestration (Heat)**)
* ``stack event``: (**Orchestration (Heat)**)
* ``stack hook``: (**Orchestration (Heat)**)
* ``stack output``: (**Orchestration (Heat)**)
* ``stack resource``: (**Orchestration (Heat)**)
* ``stack snapshot``: (**Orchestration (Heat)**)
* ``stack template``: (**Orchestration (Heat)**)
* ``subscription``: (**Messaging (Zaqar)**)
* ``task execution``: (**Workflow Engine (Mistral)**)
* ``tld``: (**DNS (Designate)**)
* ``workbook``: (**Workflow Engine (Mistral)**)
* ``workflow``: (**Workflow Engine (Mistral)**)
* ``workflow execution``: (**Workflow Engine (Mistral)**)
* ``zone``: (**DNS (Designate)**)
* ``zone blacklist``: (**DNS (Designate)**)
* ``zone export``: (**DNS (Designate)**)
* ``zone import``: (**DNS (Designate)**)
* ``zone transfer``: (**DNS (Designate)**)


Actions
-------

The actions used by OpenStackClient are defined below to provide a consistent
meaning to each action. Many of them have logical opposite actions.
Those actions with an opposite action are noted in parens if applicable.

* ``authorize`` - authorize a token (used in OAuth)
* ``add`` (``remove``) - add some object to a container object; the command
  is built in the order of ``container add object <container> <object>``,
  the positional arguments appear in the same order
* ``create`` (``delete``) - create a new occurrence of the specified object
* ``delete`` (``create``) - delete specific occurrences of the specified objects
* ``expand`` (``shrink``) - increase the capacity of a cluster
* ``failover`` - failover volume host to different backend
* ``issue`` (``revoke``) - issue a token
* ``list`` - display summary information about multiple objects
* ``lock`` (``unlock``) - lock one or more servers so that non-admin user won't be able to execute actions
* ``migrate`` - move a server or a volume to a different host; ``--live`` performs a
  live server migration if possible
* ``pause`` (``unpause``) - stop one or more servers and leave them in memory
* ``query`` - Query resources by Elasticsearch query string or json format DSL.
* ``purge`` - clean resources associated with a specific project
* ``cleanup`` - flexible clean resources associated with a specific project
* ``reboot`` - forcibly reboot a server
* ``rebuild`` - rebuild a server using (most of) the same arguments as in the original create
* ``remove`` (``add``) - remove an object from a group of objects
* ``rescue`` (``unrescue``) - reboot a server in a special rescue mode allowing access to the original disks
* ``resize`` - change a server's flavor or a cluster's capacity
* ``restore`` - restore a heat stack snapshot or restore a server in soft-deleted state
* ``resume`` (``suspend``) - return one or more suspended servers to running state
* ``revoke`` (``issue``) - revoke a token
* ``save`` - download an object locally
* ``set`` (``unset``) - set a property on the object, formerly called metadata
* ``shelve`` (``unshelve``) - shelve one or more servers
* ``show`` - display detailed information about the specific object
* ``shrink`` (``expand``) - reduce the capacity of a cluster
* ``start`` (``stop``) - start one or more servers
* ``stop`` (``start``) - stop one or more servers
* ``suspend`` (``resume``) - stop one or more servers and save to disk freeing memory
* ``unlock`` (``lock``) - unlock one or more servers
* ``unpause`` (``pause``) - return one or more paused servers to running state
* ``unrescue`` (``rescue``) - return a server to normal boot mode
* ``unset`` (``set``) - remove an attribute of the object
* ``unshelve`` (``shelve``) - unshelve one or more servers


Implementation
--------------

The command structure is designed to support seamless addition of plugin
command modules via Python's *entry points* mechanism. The plugin commands must
be subclasses of Cliff's ``command.Command`` object.  See :ref:`plugins` for
more information.


Command Entry Points
--------------------

Commands are added to the client using ``setuptools`` entry points in ``setup.cfg``.
There is a single common group ``openstack.cli`` for commands that are not versioned,
and a group for each combination of OpenStack API and version that is
supported.  For example, to support Identity API v3 there is a group called
``openstack.identity.v3`` that contains the individual commands.  The command
entry points have the form::

    action_object = fully.qualified.module.vXX.object:ActionObject

For example, the ``list user`` command for the Identity API is identified in
``setup.cfg`` with::

    openstack.identity.v3 =
        # ...
        list_user = openstackclient.identity.v3.user:ListUser
        # ...
