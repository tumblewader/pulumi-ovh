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

__all__ = ['IPLoadbalancingHTTPRouteArgs', 'IPLoadbalancingHTTPRoute']

@pulumi.input_type
class IPLoadbalancingHTTPRouteArgs:
    def __init__(__self__, *,
                 action: pulumi.Input['IPLoadbalancingHTTPRouteActionArgs'],
                 service_name: pulumi.Input[str],
                 display_name: Optional[pulumi.Input[str]] = None,
                 frontend_id: Optional[pulumi.Input[int]] = None,
                 weight: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a IPLoadbalancingHTTPRoute resource.
        :param pulumi.Input[str] service_name: The internal name of your IP load balancing
        :param pulumi.Input[str] display_name: Human readable name for your route, this field is for you
        :param pulumi.Input[int] frontend_id: Route traffic for this frontend
        :param pulumi.Input[int] weight: Route priority ([0..255]). 0 if null. Highest priority routes are evaluated first. Only the first matching route will trigger an action
               * `action.status` - HTTP status code for "redirect" and "reject" actions
               * `action.target` - Farm ID for "farm" action type or URL template for "redirect" action. You may use ${uri}, ${protocol}, ${host}, ${port} and ${path} variables in redirect target
               * `action.type` - (Required) Action to trigger if all the rules of this route matches
        """
        pulumi.set(__self__, "action", action)
        pulumi.set(__self__, "service_name", service_name)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if frontend_id is not None:
            pulumi.set(__self__, "frontend_id", frontend_id)
        if weight is not None:
            pulumi.set(__self__, "weight", weight)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Input['IPLoadbalancingHTTPRouteActionArgs']:
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: pulumi.Input['IPLoadbalancingHTTPRouteActionArgs']):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        The internal name of your IP load balancing
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Human readable name for your route, this field is for you
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="frontendId")
    def frontend_id(self) -> Optional[pulumi.Input[int]]:
        """
        Route traffic for this frontend
        """
        return pulumi.get(self, "frontend_id")

    @frontend_id.setter
    def frontend_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "frontend_id", value)

    @property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[int]]:
        """
        Route priority ([0..255]). 0 if null. Highest priority routes are evaluated first. Only the first matching route will trigger an action
        * `action.status` - HTTP status code for "redirect" and "reject" actions
        * `action.target` - Farm ID for "farm" action type or URL template for "redirect" action. You may use ${uri}, ${protocol}, ${host}, ${port} and ${path} variables in redirect target
        * `action.type` - (Required) Action to trigger if all the rules of this route matches
        """
        return pulumi.get(self, "weight")

    @weight.setter
    def weight(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "weight", value)


@pulumi.input_type
class _IPLoadbalancingHTTPRouteState:
    def __init__(__self__, *,
                 action: Optional[pulumi.Input['IPLoadbalancingHTTPRouteActionArgs']] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 frontend_id: Optional[pulumi.Input[int]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 weight: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering IPLoadbalancingHTTPRoute resources.
        :param pulumi.Input[str] display_name: Human readable name for your route, this field is for you
        :param pulumi.Input[int] frontend_id: Route traffic for this frontend
        :param pulumi.Input[str] service_name: The internal name of your IP load balancing
        :param pulumi.Input[int] weight: Route priority ([0..255]). 0 if null. Highest priority routes are evaluated first. Only the first matching route will trigger an action
               * `action.status` - HTTP status code for "redirect" and "reject" actions
               * `action.target` - Farm ID for "farm" action type or URL template for "redirect" action. You may use ${uri}, ${protocol}, ${host}, ${port} and ${path} variables in redirect target
               * `action.type` - (Required) Action to trigger if all the rules of this route matches
        """
        if action is not None:
            pulumi.set(__self__, "action", action)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if frontend_id is not None:
            pulumi.set(__self__, "frontend_id", frontend_id)
        if service_name is not None:
            pulumi.set(__self__, "service_name", service_name)
        if weight is not None:
            pulumi.set(__self__, "weight", weight)

    @property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input['IPLoadbalancingHTTPRouteActionArgs']]:
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: Optional[pulumi.Input['IPLoadbalancingHTTPRouteActionArgs']]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Human readable name for your route, this field is for you
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="frontendId")
    def frontend_id(self) -> Optional[pulumi.Input[int]]:
        """
        Route traffic for this frontend
        """
        return pulumi.get(self, "frontend_id")

    @frontend_id.setter
    def frontend_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "frontend_id", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[str]]:
        """
        The internal name of your IP load balancing
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[int]]:
        """
        Route priority ([0..255]). 0 if null. Highest priority routes are evaluated first. Only the first matching route will trigger an action
        * `action.status` - HTTP status code for "redirect" and "reject" actions
        * `action.target` - Farm ID for "farm" action type or URL template for "redirect" action. You may use ${uri}, ${protocol}, ${host}, ${port} and ${path} variables in redirect target
        * `action.type` - (Required) Action to trigger if all the rules of this route matches
        """
        return pulumi.get(self, "weight")

    @weight.setter
    def weight(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "weight", value)


class IPLoadbalancingHTTPRoute(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input[pulumi.InputType['IPLoadbalancingHTTPRouteActionArgs']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 frontend_id: Optional[pulumi.Input[int]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 weight: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Manage http route for a loadbalancer service

        ## Example Usage

        Route which redirect all url to https.

        ```python
        import pulumi
        import pulumi_ovh as ovh

        httpsredirect = ovh.IPLoadbalancingHTTPRoute("httpsredirect",
            action=ovh.IPLoadbalancingHTTPRouteActionArgs(
                status=302,
                target=f"https://{host}{path}{arguments}",
                type="redirect",
            ),
            display_name="Redirect to HTTPS",
            service_name="loadbalancer-xxxxxxxxxxxxxxxxxx",
            weight=1)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] display_name: Human readable name for your route, this field is for you
        :param pulumi.Input[int] frontend_id: Route traffic for this frontend
        :param pulumi.Input[str] service_name: The internal name of your IP load balancing
        :param pulumi.Input[int] weight: Route priority ([0..255]). 0 if null. Highest priority routes are evaluated first. Only the first matching route will trigger an action
               * `action.status` - HTTP status code for "redirect" and "reject" actions
               * `action.target` - Farm ID for "farm" action type or URL template for "redirect" action. You may use ${uri}, ${protocol}, ${host}, ${port} and ${path} variables in redirect target
               * `action.type` - (Required) Action to trigger if all the rules of this route matches
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IPLoadbalancingHTTPRouteArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manage http route for a loadbalancer service

        ## Example Usage

        Route which redirect all url to https.

        ```python
        import pulumi
        import pulumi_ovh as ovh

        httpsredirect = ovh.IPLoadbalancingHTTPRoute("httpsredirect",
            action=ovh.IPLoadbalancingHTTPRouteActionArgs(
                status=302,
                target=f"https://{host}{path}{arguments}",
                type="redirect",
            ),
            display_name="Redirect to HTTPS",
            service_name="loadbalancer-xxxxxxxxxxxxxxxxxx",
            weight=1)
        ```

        :param str resource_name: The name of the resource.
        :param IPLoadbalancingHTTPRouteArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IPLoadbalancingHTTPRouteArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input[pulumi.InputType['IPLoadbalancingHTTPRouteActionArgs']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 frontend_id: Optional[pulumi.Input[int]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 weight: Optional[pulumi.Input[int]] = None,
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
            __props__ = IPLoadbalancingHTTPRouteArgs.__new__(IPLoadbalancingHTTPRouteArgs)

            if action is None and not opts.urn:
                raise TypeError("Missing required property 'action'")
            __props__.__dict__["action"] = action
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["frontend_id"] = frontend_id
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["weight"] = weight
        super(IPLoadbalancingHTTPRoute, __self__).__init__(
            'ovh:index/iPLoadbalancingHTTPRoute:IPLoadbalancingHTTPRoute',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            action: Optional[pulumi.Input[pulumi.InputType['IPLoadbalancingHTTPRouteActionArgs']]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            frontend_id: Optional[pulumi.Input[int]] = None,
            service_name: Optional[pulumi.Input[str]] = None,
            weight: Optional[pulumi.Input[int]] = None) -> 'IPLoadbalancingHTTPRoute':
        """
        Get an existing IPLoadbalancingHTTPRoute resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] display_name: Human readable name for your route, this field is for you
        :param pulumi.Input[int] frontend_id: Route traffic for this frontend
        :param pulumi.Input[str] service_name: The internal name of your IP load balancing
        :param pulumi.Input[int] weight: Route priority ([0..255]). 0 if null. Highest priority routes are evaluated first. Only the first matching route will trigger an action
               * `action.status` - HTTP status code for "redirect" and "reject" actions
               * `action.target` - Farm ID for "farm" action type or URL template for "redirect" action. You may use ${uri}, ${protocol}, ${host}, ${port} and ${path} variables in redirect target
               * `action.type` - (Required) Action to trigger if all the rules of this route matches
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IPLoadbalancingHTTPRouteState.__new__(_IPLoadbalancingHTTPRouteState)

        __props__.__dict__["action"] = action
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["frontend_id"] = frontend_id
        __props__.__dict__["service_name"] = service_name
        __props__.__dict__["weight"] = weight
        return IPLoadbalancingHTTPRoute(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Output['outputs.IPLoadbalancingHTTPRouteAction']:
        return pulumi.get(self, "action")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        Human readable name for your route, this field is for you
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="frontendId")
    def frontend_id(self) -> pulumi.Output[int]:
        """
        Route traffic for this frontend
        """
        return pulumi.get(self, "frontend_id")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[str]:
        """
        The internal name of your IP load balancing
        """
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter
    def weight(self) -> pulumi.Output[Optional[int]]:
        """
        Route priority ([0..255]). 0 if null. Highest priority routes are evaluated first. Only the first matching route will trigger an action
        * `action.status` - HTTP status code for "redirect" and "reject" actions
        * `action.target` - Farm ID for "farm" action type or URL template for "redirect" action. You may use ${uri}, ${protocol}, ${host}, ${port} and ${path} variables in redirect target
        * `action.type` - (Required) Action to trigger if all the rules of this route matches
        """
        return pulumi.get(self, "weight")

