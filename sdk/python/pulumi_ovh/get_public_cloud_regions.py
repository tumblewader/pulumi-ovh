# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetPublicCloudRegionsResult',
    'AwaitableGetPublicCloudRegionsResult',
    'get_public_cloud_regions',
    'get_public_cloud_regions_output',
]

@pulumi.output_type
class GetPublicCloudRegionsResult:
    """
    A collection of values returned by getPublicCloudRegions.
    """
    def __init__(__self__, has_services_ups=None, id=None, names=None, project_id=None):
        if has_services_ups and not isinstance(has_services_ups, list):
            raise TypeError("Expected argument 'has_services_ups' to be a list")
        pulumi.set(__self__, "has_services_ups", has_services_ups)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        pulumi.set(__self__, "names", names)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)

    @property
    @pulumi.getter(name="hasServicesUps")
    def has_services_ups(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "has_services_ups")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def names(self) -> Sequence[str]:
        """
        The list of regions associated with the project, filtered by services UP.
        """
        return pulumi.get(self, "names")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> str:
        return pulumi.get(self, "project_id")


class AwaitableGetPublicCloudRegionsResult(GetPublicCloudRegionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPublicCloudRegionsResult(
            has_services_ups=self.has_services_ups,
            id=self.id,
            names=self.names,
            project_id=self.project_id)


def get_public_cloud_regions(has_services_ups: Optional[Sequence[str]] = None,
                             project_id: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPublicCloudRegionsResult:
    """
    > __DEPRECATED:__ Use `get_cloud_regions` instead.

    Use this data source to get the regions of a public cloud project.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_ovh as ovh

    regions = ovh.get_public_cloud_regions(has_services_ups=["network"],
        project_id="XXXXXX")
    ```


    :param Sequence[str] has_services_ups: List of services which has to be UP in regions.
           Example: "image", "instance", "network", "storage", "volume", "workflow", ...
           If left blank, returns all regions associated with the project_id.
    :param str project_id: The id of the public cloud project. If omitted,
           the `OVH_PROJECT_ID` environment variable is used.
    """
    __args__ = dict()
    __args__['hasServicesUps'] = has_services_ups
    __args__['projectId'] = project_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('ovh:index/getPublicCloudRegions:getPublicCloudRegions', __args__, opts=opts, typ=GetPublicCloudRegionsResult).value

    return AwaitableGetPublicCloudRegionsResult(
        has_services_ups=__ret__.has_services_ups,
        id=__ret__.id,
        names=__ret__.names,
        project_id=__ret__.project_id)


@_utilities.lift_output_func(get_public_cloud_regions)
def get_public_cloud_regions_output(has_services_ups: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                    project_id: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPublicCloudRegionsResult]:
    """
    > __DEPRECATED:__ Use `get_cloud_regions` instead.

    Use this data source to get the regions of a public cloud project.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_ovh as ovh

    regions = ovh.get_public_cloud_regions(has_services_ups=["network"],
        project_id="XXXXXX")
    ```


    :param Sequence[str] has_services_ups: List of services which has to be UP in regions.
           Example: "image", "instance", "network", "storage", "volume", "workflow", ...
           If left blank, returns all regions associated with the project_id.
    :param str project_id: The id of the public cloud project. If omitted,
           the `OVH_PROJECT_ID` environment variable is used.
    """
    ...
