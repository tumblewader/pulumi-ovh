# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['VRACPublicCloudAttachmentArgs', 'VRACPublicCloudAttachment']

@pulumi.input_type
class VRACPublicCloudAttachmentArgs:
    def __init__(__self__, *,
                 project_id: pulumi.Input[str],
                 vrack_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a VRACPublicCloudAttachment resource.
        :param pulumi.Input[str] project_id: The id of the public cloud project. If omitted,
               the `OVH_PROJECT_ID` environment variable is used.
        :param pulumi.Input[str] vrack_id: The id of the vrack. If omitted, the `OVH_VRACK_ID`
               environment variable is used.
        """
        pulumi.set(__self__, "project_id", project_id)
        pulumi.set(__self__, "vrack_id", vrack_id)

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
    @pulumi.getter(name="vrackId")
    def vrack_id(self) -> pulumi.Input[str]:
        """
        The id of the vrack. If omitted, the `OVH_VRACK_ID`
        environment variable is used.
        """
        return pulumi.get(self, "vrack_id")

    @vrack_id.setter
    def vrack_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "vrack_id", value)


@pulumi.input_type
class _VRACPublicCloudAttachmentState:
    def __init__(__self__, *,
                 project_id: Optional[pulumi.Input[str]] = None,
                 vrack_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering VRACPublicCloudAttachment resources.
        :param pulumi.Input[str] project_id: The id of the public cloud project. If omitted,
               the `OVH_PROJECT_ID` environment variable is used.
        :param pulumi.Input[str] vrack_id: The id of the vrack. If omitted, the `OVH_VRACK_ID`
               environment variable is used.
        """
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if vrack_id is not None:
            pulumi.set(__self__, "vrack_id", vrack_id)

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
    @pulumi.getter(name="vrackId")
    def vrack_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the vrack. If omitted, the `OVH_VRACK_ID`
        environment variable is used.
        """
        return pulumi.get(self, "vrack_id")

    @vrack_id.setter
    def vrack_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vrack_id", value)


class VRACPublicCloudAttachment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 vrack_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a VRACPublicCloudAttachment resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] project_id: The id of the public cloud project. If omitted,
               the `OVH_PROJECT_ID` environment variable is used.
        :param pulumi.Input[str] vrack_id: The id of the vrack. If omitted, the `OVH_VRACK_ID`
               environment variable is used.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VRACPublicCloudAttachmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a VRACPublicCloudAttachment resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param VRACPublicCloudAttachmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VRACPublicCloudAttachmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = VRACPublicCloudAttachmentArgs.__new__(VRACPublicCloudAttachmentArgs)

            if project_id is None and not opts.urn:
                raise TypeError("Missing required property 'project_id'")
            __props__.__dict__["project_id"] = project_id
            if vrack_id is None and not opts.urn:
                raise TypeError("Missing required property 'vrack_id'")
            __props__.__dict__["vrack_id"] = vrack_id
        super(VRACPublicCloudAttachment, __self__).__init__(
            'ovh:index/vRACPublicCloudAttachment:VRACPublicCloudAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            vrack_id: Optional[pulumi.Input[str]] = None) -> 'VRACPublicCloudAttachment':
        """
        Get an existing VRACPublicCloudAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] project_id: The id of the public cloud project. If omitted,
               the `OVH_PROJECT_ID` environment variable is used.
        :param pulumi.Input[str] vrack_id: The id of the vrack. If omitted, the `OVH_VRACK_ID`
               environment variable is used.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VRACPublicCloudAttachmentState.__new__(_VRACPublicCloudAttachmentState)

        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["vrack_id"] = vrack_id
        return VRACPublicCloudAttachment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        The id of the public cloud project. If omitted,
        the `OVH_PROJECT_ID` environment variable is used.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="vrackId")
    def vrack_id(self) -> pulumi.Output[str]:
        """
        The id of the vrack. If omitted, the `OVH_VRACK_ID`
        environment variable is used.
        """
        return pulumi.get(self, "vrack_id")

