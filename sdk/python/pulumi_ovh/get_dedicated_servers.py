# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetDedicatedServersResult',
    'AwaitableGetDedicatedServersResult',
    'get_dedicated_servers',
]

@pulumi.output_type
class GetDedicatedServersResult:
    """
    A collection of values returned by getDedicatedServers.
    """
    def __init__(__self__, id=None, results=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if results and not isinstance(results, list):
            raise TypeError("Expected argument 'results' to be a list")
        pulumi.set(__self__, "results", results)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def results(self) -> Sequence[str]:
        """
        The list of dedicated servers IDs associated with your OVH Account.
        """
        return pulumi.get(self, "results")


class AwaitableGetDedicatedServersResult(GetDedicatedServersResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDedicatedServersResult(
            id=self.id,
            results=self.results)


def get_dedicated_servers(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDedicatedServersResult:
    """
    Use this data source to get the list of dedicated servers associated with your OVH Account.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_ovh as ovh

    servers = ovh.get_dedicated_servers()
    ```
    """
    __args__ = dict()
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('ovh:index/getDedicatedServers:getDedicatedServers', __args__, opts=opts, typ=GetDedicatedServersResult).value

    return AwaitableGetDedicatedServersResult(
        id=__ret__.id,
        results=__ret__.results)
