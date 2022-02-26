// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Use this data source to get the list of Vrack network ids available for your IPLoadbalancer associated with your OVH account.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ovh from "@pulumi/ovh";
 *
 * const lbNetworks = pulumi.output(ovh.getIPLoadbalancingVRACNetworks({
 *     serviceName: "xxx",
 *     subnet: "10.0.0.0/24",
 * }));
 * ```
 */
export function getIPLoadbalancingVRACNetworks(args: GetIPLoadbalancingVRACNetworksArgs, opts?: pulumi.InvokeOptions): Promise<GetIPLoadbalancingVRACNetworksResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("ovh:index/getIPLoadbalancingVRACNetworks:getIPLoadbalancingVRACNetworks", {
        "serviceName": args.serviceName,
        "subnet": args.subnet,
        "vlanId": args.vlanId,
    }, opts);
}

/**
 * A collection of arguments for invoking getIPLoadbalancingVRACNetworks.
 */
export interface GetIPLoadbalancingVRACNetworksArgs {
    /**
     * The internal name of your IP load balancing
     */
    serviceName: string;
    /**
     * Filters networks on the subnet.
     */
    subnet?: string;
    /**
     * Filters networks on the vlan id.
     */
    vlanId?: number;
}

/**
 * A collection of values returned by getIPLoadbalancingVRACNetworks.
 */
export interface GetIPLoadbalancingVRACNetworksResult {
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * The list of vrack network ids.
     */
    readonly results: number[];
    readonly serviceName: string;
    readonly subnet?: string;
    readonly vlanId?: number;
}

export function getIPLoadbalancingVRACNetworksOutput(args: GetIPLoadbalancingVRACNetworksOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetIPLoadbalancingVRACNetworksResult> {
    return pulumi.output(args).apply(a => getIPLoadbalancingVRACNetworks(a, opts))
}

/**
 * A collection of arguments for invoking getIPLoadbalancingVRACNetworks.
 */
export interface GetIPLoadbalancingVRACNetworksOutputArgs {
    /**
     * The internal name of your IP load balancing
     */
    serviceName: pulumi.Input<string>;
    /**
     * Filters networks on the subnet.
     */
    subnet?: pulumi.Input<string>;
    /**
     * Filters networks on the vlan id.
     */
    vlanId?: pulumi.Input<number>;
}