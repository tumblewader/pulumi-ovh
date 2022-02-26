// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Use this data source to get the list of Vrack ids available for your OVH account.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ovh from "@pulumi/ovh";
 *
 * const vracks = pulumi.output(ovh.getVRACKS());
 * ```
 */
export function getVRACKS(opts?: pulumi.InvokeOptions): Promise<GetVRACKSResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("ovh:index/getVRACKS:getVRACKS", {
    }, opts);
}

/**
 * A collection of values returned by getVRACKS.
 */
export interface GetVRACKSResult {
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly results: string[];
}