// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

/**
 * Use this data source to retrieve information about a vps associated with
 * your OVH Account.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ovh from "@pulumi/ovh";
 *
 * const server = pulumi.output(ovh.getVPS({
 *     serviceName: "XXXXXX",
 * }));
 * ```
 */
export function getVPS(args: GetVPSArgs, opts?: pulumi.InvokeOptions): Promise<GetVPSResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("ovh:index/getVPS:getVPS", {
        "serviceName": args.serviceName,
    }, opts);
}

/**
 * A collection of arguments for invoking getVPS.
 */
export interface GetVPSArgs {
    /**
     * The serviceName of your dedicated server.
     */
    serviceName: string;
}

/**
 * A collection of values returned by getVPS.
 */
export interface GetVPSResult {
    /**
     * The ovh cluster the vps is in
     */
    readonly cluster: string;
    /**
     * The datacenter in which the vps is located
     * * `datacenter.longname` - The fullname of the datacenter (ex: "Strasbourg SBG1")
     * * `datacenter.name` - The short name of the datacenter (ex: "sbg1)
     */
    readonly datacenters: outputs.GetVPSDatacenter[];
    /**
     * The displayed name in the ovh web admin
     */
    readonly displayname: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * The list of IPs addresses attached to the vps
     */
    readonly ips: string[];
    /**
     * The keymap for the ip kvm, valid values "", "fr", "us"
     */
    readonly keymap: string;
    /**
     * The amount of memory in MB of the vps.
     */
    readonly memory: number;
    /**
     * A dict describing the type of vps.
     * * `model.name` - The model name (ex: model1)
     * * `model.offer` - The model human description (ex: "VPS 2016 SSD 1")
     * * `model.version` - The model version (ex: "2017v2")
     */
    readonly models: outputs.GetVPSModel[];
    readonly name: string;
    /**
     * The source of the boot kernel
     */
    readonly netbootmode: string;
    /**
     * The type of offer (ssd, cloud, classic)
     */
    readonly offertype: string;
    readonly serviceName: string;
    /**
     * A boolean to indicate if OVH sla monitoring is active.
     */
    readonly slamonitoring: boolean;
    /**
     * The state of the vps
     */
    readonly state: string;
    /**
     * The type of server
     */
    readonly type: string;
    /**
     * The number of vcore of the vps
     */
    readonly vcore: number;
    /**
     * The OVH zone where the vps is
     */
    readonly zone: string;
}

export function getVPSOutput(args: GetVPSOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetVPSResult> {
    return pulumi.output(args).apply(a => getVPS(a, opts))
}

/**
 * A collection of arguments for invoking getVPS.
 */
export interface GetVPSOutputArgs {
    /**
     * The serviceName of your dedicated server.
     */
    serviceName: pulumi.Input<string>;
}
