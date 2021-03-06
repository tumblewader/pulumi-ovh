# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['VRACDedicatedServerArgs', 'VRACDedicatedServer']

@pulumi.input_type
class VRACDedicatedServerArgs:
    def __init__(__self__, *,
                 server_id: pulumi.Input[str],
                 vrack_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a VRACDedicatedServer resource.
        :param pulumi.Input[str] server_id: The id of the dedicated server.
        :param pulumi.Input[str] vrack_id: The id of the vrack.
        """
        pulumi.set(__self__, "server_id", server_id)
        pulumi.set(__self__, "vrack_id", vrack_id)

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> pulumi.Input[str]:
        """
        The id of the dedicated server.
        """
        return pulumi.get(self, "server_id")

    @server_id.setter
    def server_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "server_id", value)

    @property
    @pulumi.getter(name="vrackId")
    def vrack_id(self) -> pulumi.Input[str]:
        """
        The id of the vrack.
        """
        return pulumi.get(self, "vrack_id")

    @vrack_id.setter
    def vrack_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "vrack_id", value)


@pulumi.input_type
class _VRACDedicatedServerState:
    def __init__(__self__, *,
                 server_id: Optional[pulumi.Input[str]] = None,
                 vrack_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering VRACDedicatedServer resources.
        :param pulumi.Input[str] server_id: The id of the dedicated server.
        :param pulumi.Input[str] vrack_id: The id of the vrack.
        """
        if server_id is not None:
            pulumi.set(__self__, "server_id", server_id)
        if vrack_id is not None:
            pulumi.set(__self__, "vrack_id", vrack_id)

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the dedicated server.
        """
        return pulumi.get(self, "server_id")

    @server_id.setter
    def server_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server_id", value)

    @property
    @pulumi.getter(name="vrackId")
    def vrack_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the vrack.
        """
        return pulumi.get(self, "vrack_id")

    @vrack_id.setter
    def vrack_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vrack_id", value)


class VRACDedicatedServer(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 server_id: Optional[pulumi.Input[str]] = None,
                 vrack_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Attach a dedicated server to a VRack.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_ovh as ovh

        vds = ovh.VRACDedicatedServer("vds",
            server_id="67890",
            vrack_id="12345")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] server_id: The id of the dedicated server.
        :param pulumi.Input[str] vrack_id: The id of the vrack.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VRACDedicatedServerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Attach a dedicated server to a VRack.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_ovh as ovh

        vds = ovh.VRACDedicatedServer("vds",
            server_id="67890",
            vrack_id="12345")
        ```

        :param str resource_name: The name of the resource.
        :param VRACDedicatedServerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VRACDedicatedServerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 server_id: Optional[pulumi.Input[str]] = None,
                 vrack_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = VRACDedicatedServerArgs.__new__(VRACDedicatedServerArgs)

            if server_id is None and not opts.urn:
                raise TypeError("Missing required property 'server_id'")
            __props__.__dict__["server_id"] = server_id
            if vrack_id is None and not opts.urn:
                raise TypeError("Missing required property 'vrack_id'")
            __props__.__dict__["vrack_id"] = vrack_id
        super(VRACDedicatedServer, __self__).__init__(
            'ovh:index/vRACDedicatedServer:VRACDedicatedServer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            server_id: Optional[pulumi.Input[str]] = None,
            vrack_id: Optional[pulumi.Input[str]] = None) -> 'VRACDedicatedServer':
        """
        Get an existing VRACDedicatedServer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] server_id: The id of the dedicated server.
        :param pulumi.Input[str] vrack_id: The id of the vrack.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VRACDedicatedServerState.__new__(_VRACDedicatedServerState)

        __props__.__dict__["server_id"] = server_id
        __props__.__dict__["vrack_id"] = vrack_id
        return VRACDedicatedServer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> pulumi.Output[str]:
        """
        The id of the dedicated server.
        """
        return pulumi.get(self, "server_id")

    @property
    @pulumi.getter(name="vrackId")
    def vrack_id(self) -> pulumi.Output[str]:
        """
        The id of the vrack.
        """
        return pulumi.get(self, "vrack_id")

