// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

/**
 * Use this data source to retrieve information about a region associated with a
 * public cloud project. The region must be associated with the project.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ovh from "@pulumi/ovh";
 *
 * const gRA1 = pulumi.output(ovh.getCloudRegion({
 *     name: "GRA1",
 *     projectId: "XXXXXX",
 * }));
 * ```
 */
export function getCloudRegion(args: GetCloudRegionArgs, opts?: pulumi.InvokeOptions): Promise<GetCloudRegionResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("ovh:index/getCloudRegion:getCloudRegion", {
        "name": args.name,
        "projectId": args.projectId,
    }, opts);
}

/**
 * A collection of arguments for invoking getCloudRegion.
 */
export interface GetCloudRegionArgs {
    /**
     * The name of the region associated with the public cloud
     * project.
     */
    name: string;
    /**
     * The id of the public cloud project. If omitted,
     * the `OVH_PROJECT_ID` environment variable is used.
     */
    projectId: string;
}

/**
 * A collection of values returned by getCloudRegion.
 */
export interface GetCloudRegionResult {
    /**
     * the code of the geographic continent the region is running.
     * E.g.: EU for Europe, US for America...
     */
    readonly continentCode: string;
    /**
     * The location code of the datacenter.
     * E.g.: "GRA", meaning Gravelines, for region "GRA1"
     */
    readonly datacenterLocation: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * the name of the public cloud service
     */
    readonly name: string;
    readonly projectId: string;
    /**
     * The list of public cloud services running within the region
     */
    readonly services: outputs.GetCloudRegionService[];
}

export function getCloudRegionOutput(args: GetCloudRegionOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetCloudRegionResult> {
    return pulumi.output(args).apply(a => getCloudRegion(a, opts))
}

/**
 * A collection of arguments for invoking getCloudRegion.
 */
export interface GetCloudRegionOutputArgs {
    /**
     * The name of the region associated with the public cloud
     * project.
     */
    name: pulumi.Input<string>;
    /**
     * The id of the public cloud project. If omitted,
     * the `OVH_PROJECT_ID` environment variable is used.
     */
    projectId: pulumi.Input<string>;
}