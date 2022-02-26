# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['CloudNetworkPrivateArgs', 'CloudNetworkPrivate']

@pulumi.input_type
class CloudNetworkPrivateArgs:
    def __init__(__self__, *,
                 project_id: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 regions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 vlan_id: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a CloudNetworkPrivate resource.
        :param pulumi.Input[str] project_id: The id of the public cloud project. If omitted,
               the `OVH_PROJECT_ID` environment variable is used.
        :param pulumi.Input[str] name: The name of the network.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] regions: an array of valid OVH public cloud region ID in which the network
               will be available. Ex.: "GRA1". Defaults to all public cloud regions.
        :param pulumi.Input[int] vlan_id: a vlan id to associate with the network.
               Changing this value recreates the resource. Defaults to 0.
        """
        pulumi.set(__self__, "project_id", project_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if regions is not None:
            pulumi.set(__self__, "regions", regions)
        if vlan_id is not None:
            pulumi.set(__self__, "vlan_id", vlan_id)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[str]:
        """
        The id of the public cloud project. If omitted,
        the `OVH_PROJECT_ID` environment variable is used.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the network.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def regions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        an array of valid OVH public cloud region ID in which the network
        will be available. Ex.: "GRA1". Defaults to all public cloud regions.
        """
        return pulumi.get(self, "regions")

    @regions.setter
    def regions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "regions", value)

    @property
    @pulumi.getter(name="vlanId")
    def vlan_id(self) -> Optional[pulumi.Input[int]]:
        """
        a vlan id to associate with the network.
        Changing this value recreates the resource. Defaults to 0.
        """
        return pulumi.get(self, "vlan_id")

    @vlan_id.setter
    def vlan_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "vlan_id", value)


@pulumi.input_type
class _CloudNetworkPrivateState:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 regions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 regions_statuses: Optional[pulumi.Input[Sequence[pulumi.Input['CloudNetworkPrivateRegionsStatusArgs']]]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 vlan_id: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering CloudNetworkPrivate resources.
        :param pulumi.Input[str] name: The name of the network.
        :param pulumi.Input[str] project_id: The id of the public cloud project. If omitted,
               the `OVH_PROJECT_ID` environment variable is used.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] regions: an array of valid OVH public cloud region ID in which the network
               will be available. Ex.: "GRA1". Defaults to all public cloud regions.
        :param pulumi.Input[Sequence[pulumi.Input['CloudNetworkPrivateRegionsStatusArgs']]] regions_statuses: A map representing the status of the network per region.
               * `regions_status/region` - The id of the region.
               * `regions_status/status` - The status of the network in the region.
        :param pulumi.Input[str] status: the status of the network. should be normally set to 'ACTIVE'.
        :param pulumi.Input[str] type: the type of the network. Either 'private' or 'public'.
        :param pulumi.Input[int] vlan_id: a vlan id to associate with the network.
               Changing this value recreates the resource. Defaults to 0.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if regions is not None:
            pulumi.set(__self__, "regions", regions)
        if regions_statuses is not None:
            pulumi.set(__self__, "regions_statuses", regions_statuses)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if vlan_id is not None:
            pulumi.set(__self__, "vlan_id", vlan_id)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the network.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the public cloud project. If omitted,
        the `OVH_PROJECT_ID` environment variable is used.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter
    def regions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        an array of valid OVH public cloud region ID in which the network
        will be available. Ex.: "GRA1". Defaults to all public cloud regions.
        """
        return pulumi.get(self, "regions")

    @regions.setter
    def regions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "regions", value)

    @property
    @pulumi.getter(name="regionsStatuses")
    def regions_statuses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CloudNetworkPrivateRegionsStatusArgs']]]]:
        """
        A map representing the status of the network per region.
        * `regions_status/region` - The id of the region.
        * `regions_status/status` - The status of the network in the region.
        """
        return pulumi.get(self, "regions_statuses")

    @regions_statuses.setter
    def regions_statuses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CloudNetworkPrivateRegionsStatusArgs']]]]):
        pulumi.set(self, "regions_statuses", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        the status of the network. should be normally set to 'ACTIVE'.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        the type of the network. Either 'private' or 'public'.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="vlanId")
    def vlan_id(self) -> Optional[pulumi.Input[int]]:
        """
        a vlan id to associate with the network.
        Changing this value recreates the resource. Defaults to 0.
        """
        return pulumi.get(self, "vlan_id")

    @vlan_id.setter
    def vlan_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "vlan_id", value)


class CloudNetworkPrivate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 regions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 vlan_id: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Creates a private network in a public cloud project.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_ovh as ovh

        net = ovh.CloudNetworkPrivate("net",
            project_id="67890",
            regions=[
                "GRA1",
                "BHS1",
            ])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of the network.
        :param pulumi.Input[str] project_id: The id of the public cloud project. If omitted,
               the `OVH_PROJECT_ID` environment variable is used.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] regions: an array of valid OVH public cloud region ID in which the network
               will be available. Ex.: "GRA1". Defaults to all public cloud regions.
        :param pulumi.Input[int] vlan_id: a vlan id to associate with the network.
               Changing this value recreates the resource. Defaults to 0.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CloudNetworkPrivateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a private network in a public cloud project.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_ovh as ovh

        net = ovh.CloudNetworkPrivate("net",
            project_id="67890",
            regions=[
                "GRA1",
                "BHS1",
            ])
        ```

        :param str resource_name: The name of the resource.
        :param CloudNetworkPrivateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CloudNetworkPrivateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 regions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 vlan_id: Optional[pulumi.Input[int]] = None,
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
            __props__ = CloudNetworkPrivateArgs.__new__(CloudNetworkPrivateArgs)

            __props__.__dict__["name"] = name
            if project_id is None and not opts.urn:
                raise TypeError("Missing required property 'project_id'")
            __props__.__dict__["project_id"] = project_id
            __props__.__dict__["regions"] = regions
            __props__.__dict__["vlan_id"] = vlan_id
            __props__.__dict__["regions_statuses"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["type"] = None
        super(CloudNetworkPrivate, __self__).__init__(
            'ovh:index/cloudNetworkPrivate:CloudNetworkPrivate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            name: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            regions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            regions_statuses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CloudNetworkPrivateRegionsStatusArgs']]]]] = None,
            status: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None,
            vlan_id: Optional[pulumi.Input[int]] = None) -> 'CloudNetworkPrivate':
        """
        Get an existing CloudNetworkPrivate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of the network.
        :param pulumi.Input[str] project_id: The id of the public cloud project. If omitted,
               the `OVH_PROJECT_ID` environment variable is used.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] regions: an array of valid OVH public cloud region ID in which the network
               will be available. Ex.: "GRA1". Defaults to all public cloud regions.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CloudNetworkPrivateRegionsStatusArgs']]]] regions_statuses: A map representing the status of the network per region.
               * `regions_status/region` - The id of the region.
               * `regions_status/status` - The status of the network in the region.
        :param pulumi.Input[str] status: the status of the network. should be normally set to 'ACTIVE'.
        :param pulumi.Input[str] type: the type of the network. Either 'private' or 'public'.
        :param pulumi.Input[int] vlan_id: a vlan id to associate with the network.
               Changing this value recreates the resource. Defaults to 0.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CloudNetworkPrivateState.__new__(_CloudNetworkPrivateState)

        __props__.__dict__["name"] = name
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["regions"] = regions
        __props__.__dict__["regions_statuses"] = regions_statuses
        __props__.__dict__["status"] = status
        __props__.__dict__["type"] = type
        __props__.__dict__["vlan_id"] = vlan_id
        return CloudNetworkPrivate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the network.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        The id of the public cloud project. If omitted,
        the `OVH_PROJECT_ID` environment variable is used.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def regions(self) -> pulumi.Output[Sequence[str]]:
        """
        an array of valid OVH public cloud region ID in which the network
        will be available. Ex.: "GRA1". Defaults to all public cloud regions.
        """
        return pulumi.get(self, "regions")

    @property
    @pulumi.getter(name="regionsStatuses")
    def regions_statuses(self) -> pulumi.Output[Sequence['outputs.CloudNetworkPrivateRegionsStatus']]:
        """
        A map representing the status of the network per region.
        * `regions_status/region` - The id of the region.
        * `regions_status/status` - The status of the network in the region.
        """
        return pulumi.get(self, "regions_statuses")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        the status of the network. should be normally set to 'ACTIVE'.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        the type of the network. Either 'private' or 'public'.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vlanId")
    def vlan_id(self) -> pulumi.Output[Optional[int]]:
        """
        a vlan id to associate with the network.
        Changing this value recreates the resource. Defaults to 0.
        """
        return pulumi.get(self, "vlan_id")

