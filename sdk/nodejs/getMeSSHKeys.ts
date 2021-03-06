// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Use this data source to retrieve list of names of the account's SSH keys.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ovh from "@pulumi/ovh";
 *
 * const mykeys = pulumi.output(ovh.getMeSSHKeys());
 * ```
 */
export function getMeSSHKeys(opts?: pulumi.InvokeOptions): Promise<GetMeSSHKeysResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("ovh:index/getMeSSHKeys:getMeSSHKeys", {
    }, opts);
}

/**
 * A collection of values returned by getMeSSHKeys.
 */
export interface GetMeSSHKeysResult {
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * The list of the names of all the SSH keys.
     */
    readonly names: string[];
}
