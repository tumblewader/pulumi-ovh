# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'GetDedicatedServerResult',
    'AwaitableGetDedicatedServerResult',
    'get_dedicated_server',
    'get_dedicated_server_output',
]

@pulumi.output_type
class GetDedicatedServerResult:
    """
    A collection of values returned by getDedicatedServer.
    """
    def __init__(__self__, boot_id=None, commercial_range=None, datacenter=None, enabled_public_vnis=None, enabled_vrack_aggregation_vnis=None, enabled_vrack_vnis=None, id=None, ip=None, ips=None, link_speed=None, monitoring=None, name=None, os=None, professional_use=None, rack=None, rescue_mail=None, reverse=None, root_device=None, server_id=None, service_name=None, state=None, support_level=None, vnis=None):
        if boot_id and not isinstance(boot_id, int):
            raise TypeError("Expected argument 'boot_id' to be a int")
        pulumi.set(__self__, "boot_id", boot_id)
        if commercial_range and not isinstance(commercial_range, str):
            raise TypeError("Expected argument 'commercial_range' to be a str")
        pulumi.set(__self__, "commercial_range", commercial_range)
        if datacenter and not isinstance(datacenter, str):
            raise TypeError("Expected argument 'datacenter' to be a str")
        pulumi.set(__self__, "datacenter", datacenter)
        if enabled_public_vnis and not isinstance(enabled_public_vnis, list):
            raise TypeError("Expected argument 'enabled_public_vnis' to be a list")
        pulumi.set(__self__, "enabled_public_vnis", enabled_public_vnis)
        if enabled_vrack_aggregation_vnis and not isinstance(enabled_vrack_aggregation_vnis, list):
            raise TypeError("Expected argument 'enabled_vrack_aggregation_vnis' to be a list")
        pulumi.set(__self__, "enabled_vrack_aggregation_vnis", enabled_vrack_aggregation_vnis)
        if enabled_vrack_vnis and not isinstance(enabled_vrack_vnis, list):
            raise TypeError("Expected argument 'enabled_vrack_vnis' to be a list")
        pulumi.set(__self__, "enabled_vrack_vnis", enabled_vrack_vnis)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ip and not isinstance(ip, str):
            raise TypeError("Expected argument 'ip' to be a str")
        pulumi.set(__self__, "ip", ip)
        if ips and not isinstance(ips, list):
            raise TypeError("Expected argument 'ips' to be a list")
        pulumi.set(__self__, "ips", ips)
        if link_speed and not isinstance(link_speed, int):
            raise TypeError("Expected argument 'link_speed' to be a int")
        pulumi.set(__self__, "link_speed", link_speed)
        if monitoring and not isinstance(monitoring, bool):
            raise TypeError("Expected argument 'monitoring' to be a bool")
        pulumi.set(__self__, "monitoring", monitoring)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if os and not isinstance(os, str):
            raise TypeError("Expected argument 'os' to be a str")
        pulumi.set(__self__, "os", os)
        if professional_use and not isinstance(professional_use, bool):
            raise TypeError("Expected argument 'professional_use' to be a bool")
        pulumi.set(__self__, "professional_use", professional_use)
        if rack and not isinstance(rack, str):
            raise TypeError("Expected argument 'rack' to be a str")
        pulumi.set(__self__, "rack", rack)
        if rescue_mail and not isinstance(rescue_mail, str):
            raise TypeError("Expected argument 'rescue_mail' to be a str")
        pulumi.set(__self__, "rescue_mail", rescue_mail)
        if reverse and not isinstance(reverse, str):
            raise TypeError("Expected argument 'reverse' to be a str")
        pulumi.set(__self__, "reverse", reverse)
        if root_device and not isinstance(root_device, str):
            raise TypeError("Expected argument 'root_device' to be a str")
        pulumi.set(__self__, "root_device", root_device)
        if server_id and not isinstance(server_id, int):
            raise TypeError("Expected argument 'server_id' to be a int")
        pulumi.set(__self__, "server_id", server_id)
        if service_name and not isinstance(service_name, str):
            raise TypeError("Expected argument 'service_name' to be a str")
        pulumi.set(__self__, "service_name", service_name)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if support_level and not isinstance(support_level, str):
            raise TypeError("Expected argument 'support_level' to be a str")
        pulumi.set(__self__, "support_level", support_level)
        if vnis and not isinstance(vnis, list):
            raise TypeError("Expected argument 'vnis' to be a list")
        pulumi.set(__self__, "vnis", vnis)

    @property
    @pulumi.getter(name="bootId")
    def boot_id(self) -> int:
        """
        boot id of the server
        """
        return pulumi.get(self, "boot_id")

    @property
    @pulumi.getter(name="commercialRange")
    def commercial_range(self) -> str:
        """
        dedicater server commercial range
        """
        return pulumi.get(self, "commercial_range")

    @property
    @pulumi.getter
    def datacenter(self) -> str:
        """
        dedicated datacenter localisation (bhs1,bhs2,...)
        """
        return pulumi.get(self, "datacenter")

    @property
    @pulumi.getter(name="enabledPublicVnis")
    def enabled_public_vnis(self) -> Sequence[str]:
        """
        List of enabled public VNI uuids
        """
        return pulumi.get(self, "enabled_public_vnis")

    @property
    @pulumi.getter(name="enabledVrackAggregationVnis")
    def enabled_vrack_aggregation_vnis(self) -> Sequence[str]:
        """
        List of enabled vrack_aggregation VNI uuids
        """
        return pulumi.get(self, "enabled_vrack_aggregation_vnis")

    @property
    @pulumi.getter(name="enabledVrackVnis")
    def enabled_vrack_vnis(self) -> Sequence[str]:
        """
        List of enabled vrack VNI uuids
        """
        return pulumi.get(self, "enabled_vrack_vnis")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ip(self) -> str:
        """
        dedicated server ip (IPv4)
        """
        return pulumi.get(self, "ip")

    @property
    @pulumi.getter
    def ips(self) -> Sequence[str]:
        """
        dedicated server ip blocks
        """
        return pulumi.get(self, "ips")

    @property
    @pulumi.getter(name="linkSpeed")
    def link_speed(self) -> int:
        """
        link speed of the server
        """
        return pulumi.get(self, "link_speed")

    @property
    @pulumi.getter
    def monitoring(self) -> bool:
        """
        Icmp monitoring state
        """
        return pulumi.get(self, "monitoring")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        User defined VirtualNetworkInterface name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def os(self) -> str:
        """
        Operating system
        """
        return pulumi.get(self, "os")

    @property
    @pulumi.getter(name="professionalUse")
    def professional_use(self) -> bool:
        """
        Does this server have professional use option
        """
        return pulumi.get(self, "professional_use")

    @property
    @pulumi.getter
    def rack(self) -> str:
        """
        rack id of the server
        """
        return pulumi.get(self, "rack")

    @property
    @pulumi.getter(name="rescueMail")
    def rescue_mail(self) -> str:
        """
        rescue mail of the server
        """
        return pulumi.get(self, "rescue_mail")

    @property
    @pulumi.getter
    def reverse(self) -> str:
        """
        dedicated server reverse
        """
        return pulumi.get(self, "reverse")

    @property
    @pulumi.getter(name="rootDevice")
    def root_device(self) -> str:
        """
        root device of the server
        """
        return pulumi.get(self, "root_device")

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> int:
        """
        your server id
        """
        return pulumi.get(self, "server_id")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> str:
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        error, hacked, hackedBlocked, ok
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="supportLevel")
    def support_level(self) -> str:
        """
        Dedicated server support level (critical, fastpath, gs, pro)
        """
        return pulumi.get(self, "support_level")

    @property
    @pulumi.getter
    def vnis(self) -> Sequence['outputs.GetDedicatedServerVniResult']:
        """
        the list of Virtualnetworkinterface assiociated with this server
        """
        return pulumi.get(self, "vnis")


class AwaitableGetDedicatedServerResult(GetDedicatedServerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDedicatedServerResult(
            boot_id=self.boot_id,
            commercial_range=self.commercial_range,
            datacenter=self.datacenter,
            enabled_public_vnis=self.enabled_public_vnis,
            enabled_vrack_aggregation_vnis=self.enabled_vrack_aggregation_vnis,
            enabled_vrack_vnis=self.enabled_vrack_vnis,
            id=self.id,
            ip=self.ip,
            ips=self.ips,
            link_speed=self.link_speed,
            monitoring=self.monitoring,
            name=self.name,
            os=self.os,
            professional_use=self.professional_use,
            rack=self.rack,
            rescue_mail=self.rescue_mail,
            reverse=self.reverse,
            root_device=self.root_device,
            server_id=self.server_id,
            service_name=self.service_name,
            state=self.state,
            support_level=self.support_level,
            vnis=self.vnis)


def get_dedicated_server(service_name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDedicatedServerResult:
    """
    Use this data source to retrieve information about a dedicated server associated with
    your OVH Account.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_ovh as ovh

    server = ovh.get_dedicated_server(service_name="XXXXXX")
    ```


    :param str service_name: The service_name of your dedicated server.
    """
    __args__ = dict()
    __args__['serviceName'] = service_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('ovh:index/getDedicatedServer:getDedicatedServer', __args__, opts=opts, typ=GetDedicatedServerResult).value

    return AwaitableGetDedicatedServerResult(
        boot_id=__ret__.boot_id,
        commercial_range=__ret__.commercial_range,
        datacenter=__ret__.datacenter,
        enabled_public_vnis=__ret__.enabled_public_vnis,
        enabled_vrack_aggregation_vnis=__ret__.enabled_vrack_aggregation_vnis,
        enabled_vrack_vnis=__ret__.enabled_vrack_vnis,
        id=__ret__.id,
        ip=__ret__.ip,
        ips=__ret__.ips,
        link_speed=__ret__.link_speed,
        monitoring=__ret__.monitoring,
        name=__ret__.name,
        os=__ret__.os,
        professional_use=__ret__.professional_use,
        rack=__ret__.rack,
        rescue_mail=__ret__.rescue_mail,
        reverse=__ret__.reverse,
        root_device=__ret__.root_device,
        server_id=__ret__.server_id,
        service_name=__ret__.service_name,
        state=__ret__.state,
        support_level=__ret__.support_level,
        vnis=__ret__.vnis)


@_utilities.lift_output_func(get_dedicated_server)
def get_dedicated_server_output(service_name: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDedicatedServerResult]:
    """
    Use this data source to retrieve information about a dedicated server associated with
    your OVH Account.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_ovh as ovh

    server = ovh.get_dedicated_server(service_name="XXXXXX")
    ```


    :param str service_name: The service_name of your dedicated server.
    """
    ...
