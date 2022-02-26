// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Use this data source to retrieve information about a bank account
 * payment mean associated with an OVH account.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ovh from "@pulumi/ovh";
 *
 * const ba = pulumi.output(ovh.getMePaymentMeanBankAccount({
 *     useDefault: true,
 * }));
 * ```
 */
export function getMePaymentMeanBankAccount(args?: GetMePaymentMeanBankAccountArgs, opts?: pulumi.InvokeOptions): Promise<GetMePaymentMeanBankAccountResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("ovh:index/getMePaymentMeanBankAccount:getMePaymentMeanBankAccount", {
        "descriptionRegexp": args.descriptionRegexp,
        "state": args.state,
        "useDefault": args.useDefault,
        "useOldest": args.useOldest,
    }, opts);
}

/**
 * A collection of arguments for invoking getMePaymentMeanBankAccount.
 */
export interface GetMePaymentMeanBankAccountArgs {
    /**
     * a regexp used to filter bank accounts 
     * on their `description` attributes.
     */
    descriptionRegexp?: string;
    /**
     * Filter bank accounts on their `state` attribute.
     * Can be "blockedForIncidents", "valid", "pendingValidation"
     */
    state?: string;
    /**
     * Retrieve bank account marked as default payment mean.
     */
    useDefault?: boolean;
    /**
     * Retrieve oldest bank account.
     * project.
     */
    useOldest?: boolean;
}

/**
 * A collection of values returned by getMePaymentMeanBankAccount.
 */
export interface GetMePaymentMeanBankAccountResult {
    /**
     * a boolean which tells if the retrieved bank account
     * is marked as the default payment mean
     */
    readonly default: boolean;
    /**
     * the description attribute of the bank account
     */
    readonly description: string;
    readonly descriptionRegexp?: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly state: string;
    readonly useDefault?: boolean;
    readonly useOldest?: boolean;
}

export function getMePaymentMeanBankAccountOutput(args?: GetMePaymentMeanBankAccountOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetMePaymentMeanBankAccountResult> {
    return pulumi.output(args).apply(a => getMePaymentMeanBankAccount(a, opts))
}

/**
 * A collection of arguments for invoking getMePaymentMeanBankAccount.
 */
export interface GetMePaymentMeanBankAccountOutputArgs {
    /**
     * a regexp used to filter bank accounts 
     * on their `description` attributes.
     */
    descriptionRegexp?: pulumi.Input<string>;
    /**
     * Filter bank accounts on their `state` attribute.
     * Can be "blockedForIncidents", "valid", "pendingValidation"
     */
    state?: pulumi.Input<string>;
    /**
     * Retrieve bank account marked as default payment mean.
     */
    useDefault?: pulumi.Input<boolean>;
    /**
     * Retrieve oldest bank account.
     * project.
     */
    useOldest?: pulumi.Input<boolean>;
}
