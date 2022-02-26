# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['DomainZoneRedirectionArgs', 'DomainZoneRedirection']

@pulumi.input_type
class DomainZoneRedirectionArgs:
    def __init__(__self__, *,
                 target: pulumi.Input[str],
                 type: pulumi.Input[str],
                 zone: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 keywords: Optional[pulumi.Input[str]] = None,
                 subdomain: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DomainZoneRedirection resource.
        :param pulumi.Input[str] target: The value of the redirection
        :param pulumi.Input[str] type: The type of the redirection, with values:
        :param pulumi.Input[str] zone: The domain to add the redirection to
        :param pulumi.Input[str] description: A description of this redirection
        :param pulumi.Input[str] keywords: Keywords to describe this redirection
        :param pulumi.Input[str] subdomain: The name of the redirection
        :param pulumi.Input[str] title: Title of this redirection
        """
        pulumi.set(__self__, "target", target)
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "zone", zone)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if keywords is not None:
            pulumi.set(__self__, "keywords", keywords)
        if subdomain is not None:
            pulumi.set(__self__, "subdomain", subdomain)
        if title is not None:
            pulumi.set(__self__, "title", title)

    @property
    @pulumi.getter
    def target(self) -> pulumi.Input[str]:
        """
        The value of the redirection
        """
        return pulumi.get(self, "target")

    @target.setter
    def target(self, value: pulumi.Input[str]):
        pulumi.set(self, "target", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of the redirection, with values:
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def zone(self) -> pulumi.Input[str]:
        """
        The domain to add the redirection to
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: pulumi.Input[str]):
        pulumi.set(self, "zone", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description of this redirection
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def keywords(self) -> Optional[pulumi.Input[str]]:
        """
        Keywords to describe this redirection
        """
        return pulumi.get(self, "keywords")

    @keywords.setter
    def keywords(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "keywords", value)

    @property
    @pulumi.getter
    def subdomain(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the redirection
        """
        return pulumi.get(self, "subdomain")

    @subdomain.setter
    def subdomain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subdomain", value)

    @property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[str]]:
        """
        Title of this redirection
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "title", value)


@pulumi.input_type
class _DomainZoneRedirectionState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 keywords: Optional[pulumi.Input[str]] = None,
                 subdomain: Optional[pulumi.Input[str]] = None,
                 target: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DomainZoneRedirection resources.
        :param pulumi.Input[str] description: A description of this redirection
        :param pulumi.Input[str] keywords: Keywords to describe this redirection
        :param pulumi.Input[str] subdomain: The name of the redirection
        :param pulumi.Input[str] target: The value of the redirection
        :param pulumi.Input[str] title: Title of this redirection
        :param pulumi.Input[str] type: The type of the redirection, with values:
        :param pulumi.Input[str] zone: The domain to add the redirection to
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if keywords is not None:
            pulumi.set(__self__, "keywords", keywords)
        if subdomain is not None:
            pulumi.set(__self__, "subdomain", subdomain)
        if target is not None:
            pulumi.set(__self__, "target", target)
        if title is not None:
            pulumi.set(__self__, "title", title)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description of this redirection
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def keywords(self) -> Optional[pulumi.Input[str]]:
        """
        Keywords to describe this redirection
        """
        return pulumi.get(self, "keywords")

    @keywords.setter
    def keywords(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "keywords", value)

    @property
    @pulumi.getter
    def subdomain(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the redirection
        """
        return pulumi.get(self, "subdomain")

    @subdomain.setter
    def subdomain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subdomain", value)

    @property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[str]]:
        """
        The value of the redirection
        """
        return pulumi.get(self, "target")

    @target.setter
    def target(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target", value)

    @property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[str]]:
        """
        Title of this redirection
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the redirection, with values:
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[str]]:
        """
        The domain to add the redirection to
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone", value)


class DomainZoneRedirection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 keywords: Optional[pulumi.Input[str]] = None,
                 subdomain: Optional[pulumi.Input[str]] = None,
                 target: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a OVH domain zone redirection.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_ovh as ovh

        # Add a redirection to a sub-domain
        test = ovh.DomainZoneRedirection("test",
            subdomain="test",
            target="http://www.ovh",
            type="visiblePermanent",
            zone="testdemo.ovh")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A description of this redirection
        :param pulumi.Input[str] keywords: Keywords to describe this redirection
        :param pulumi.Input[str] subdomain: The name of the redirection
        :param pulumi.Input[str] target: The value of the redirection
        :param pulumi.Input[str] title: Title of this redirection
        :param pulumi.Input[str] type: The type of the redirection, with values:
        :param pulumi.Input[str] zone: The domain to add the redirection to
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DomainZoneRedirectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a OVH domain zone redirection.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_ovh as ovh

        # Add a redirection to a sub-domain
        test = ovh.DomainZoneRedirection("test",
            subdomain="test",
            target="http://www.ovh",
            type="visiblePermanent",
            zone="testdemo.ovh")
        ```

        :param str resource_name: The name of the resource.
        :param DomainZoneRedirectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DomainZoneRedirectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 keywords: Optional[pulumi.Input[str]] = None,
                 subdomain: Optional[pulumi.Input[str]] = None,
                 target: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DomainZoneRedirectionArgs.__new__(DomainZoneRedirectionArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["keywords"] = keywords
            __props__.__dict__["subdomain"] = subdomain
            if target is None and not opts.urn:
                raise TypeError("Missing required property 'target'")
            __props__.__dict__["target"] = target
            __props__.__dict__["title"] = title
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            if zone is None and not opts.urn:
                raise TypeError("Missing required property 'zone'")
            __props__.__dict__["zone"] = zone
        super(DomainZoneRedirection, __self__).__init__(
            'ovh:index/domainZoneRedirection:DomainZoneRedirection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            keywords: Optional[pulumi.Input[str]] = None,
            subdomain: Optional[pulumi.Input[str]] = None,
            target: Optional[pulumi.Input[str]] = None,
            title: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None,
            zone: Optional[pulumi.Input[str]] = None) -> 'DomainZoneRedirection':
        """
        Get an existing DomainZoneRedirection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A description of this redirection
        :param pulumi.Input[str] keywords: Keywords to describe this redirection
        :param pulumi.Input[str] subdomain: The name of the redirection
        :param pulumi.Input[str] target: The value of the redirection
        :param pulumi.Input[str] title: Title of this redirection
        :param pulumi.Input[str] type: The type of the redirection, with values:
        :param pulumi.Input[str] zone: The domain to add the redirection to
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DomainZoneRedirectionState.__new__(_DomainZoneRedirectionState)

        __props__.__dict__["description"] = description
        __props__.__dict__["keywords"] = keywords
        __props__.__dict__["subdomain"] = subdomain
        __props__.__dict__["target"] = target
        __props__.__dict__["title"] = title
        __props__.__dict__["type"] = type
        __props__.__dict__["zone"] = zone
        return DomainZoneRedirection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description of this redirection
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def keywords(self) -> pulumi.Output[Optional[str]]:
        """
        Keywords to describe this redirection
        """
        return pulumi.get(self, "keywords")

    @property
    @pulumi.getter
    def subdomain(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the redirection
        """
        return pulumi.get(self, "subdomain")

    @property
    @pulumi.getter
    def target(self) -> pulumi.Output[str]:
        """
        The value of the redirection
        """
        return pulumi.get(self, "target")

    @property
    @pulumi.getter
    def title(self) -> pulumi.Output[Optional[str]]:
        """
        Title of this redirection
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the redirection, with values:
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def zone(self) -> pulumi.Output[str]:
        """
        The domain to add the redirection to
        """
        return pulumi.get(self, "zone")

