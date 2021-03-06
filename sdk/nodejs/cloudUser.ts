// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

/**
 * Creates a user in a public cloud project.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ovh from "@pulumi/ovh";
 *
 * const user1 = new ovh.CloudUser("user1", {
 *     projectId: "67890",
 * });
 * ```
 */
export class CloudUser extends pulumi.CustomResource {
    /**
     * Get an existing CloudUser resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CloudUserState, opts?: pulumi.CustomResourceOptions): CloudUser {
        return new CloudUser(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ovh:index/cloudUser:CloudUser';

    /**
     * Returns true if the given object is an instance of CloudUser.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is CloudUser {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === CloudUser.__pulumiType;
    }

    /**
     * the date the user was created.
     */
    public /*out*/ readonly creationDate!: pulumi.Output<string>;
    /**
     * A description associated with the user.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * a convenient map representing an openstackRc file.
     * Note: no password nor sensitive token is set in this map.
     */
    public readonly openstackRc!: pulumi.Output<{[key: string]: any}>;
    /**
     * (Sensitive) the password generated for the user. The password can
     * be used with the Openstack API. This attribute is sensitive and will only be
     * retrieve once during creation.
     */
    public /*out*/ readonly password!: pulumi.Output<string>;
    /**
     * The id of the public cloud project. If omitted,
     * the `OVH_PROJECT_ID` environment variable is used. DEPRECATED. Use `serviceName` instead.
     */
    public readonly projectId!: pulumi.Output<string | undefined>;
    /**
     * The name of a role. See `roleNames`.
     */
    public readonly roleName!: pulumi.Output<string | undefined>;
    /**
     * A list of role names. Values can be: 
     * - administrator,
     * - aiTrainingOperator
     * - authentication
     * - backupOperator
     * - computeOperator
     * - imageOperator
     * - infrastructureSupervisor
     * - networkOperator
     * - networkSecurityOperator
     * - objectstoreOperator
     * - volume_operator
     */
    public readonly roleNames!: pulumi.Output<string[] | undefined>;
    /**
     * A list of roles associated with the user.
     */
    public /*out*/ readonly roles!: pulumi.Output<outputs.CloudUserRole[]>;
    /**
     * The id of the public cloud project. Conflicts with `projectId`.
     */
    public readonly serviceName!: pulumi.Output<string | undefined>;
    /**
     * the status of the user. should be normally set to 'ok'.
     */
    public /*out*/ readonly status!: pulumi.Output<string>;
    /**
     * the username generated for the user. This username can be used with
     * the Openstack API.
     */
    public /*out*/ readonly username!: pulumi.Output<string>;

    /**
     * Create a CloudUser resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: CloudUserArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: CloudUserArgs | CloudUserState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as CloudUserState | undefined;
            resourceInputs["creationDate"] = state ? state.creationDate : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["openstackRc"] = state ? state.openstackRc : undefined;
            resourceInputs["password"] = state ? state.password : undefined;
            resourceInputs["projectId"] = state ? state.projectId : undefined;
            resourceInputs["roleName"] = state ? state.roleName : undefined;
            resourceInputs["roleNames"] = state ? state.roleNames : undefined;
            resourceInputs["roles"] = state ? state.roles : undefined;
            resourceInputs["serviceName"] = state ? state.serviceName : undefined;
            resourceInputs["status"] = state ? state.status : undefined;
            resourceInputs["username"] = state ? state.username : undefined;
        } else {
            const args = argsOrState as CloudUserArgs | undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["openstackRc"] = args ? args.openstackRc : undefined;
            resourceInputs["projectId"] = args ? args.projectId : undefined;
            resourceInputs["roleName"] = args ? args.roleName : undefined;
            resourceInputs["roleNames"] = args ? args.roleNames : undefined;
            resourceInputs["serviceName"] = args ? args.serviceName : undefined;
            resourceInputs["creationDate"] = undefined /*out*/;
            resourceInputs["password"] = undefined /*out*/;
            resourceInputs["roles"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
            resourceInputs["username"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(CloudUser.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering CloudUser resources.
 */
export interface CloudUserState {
    /**
     * the date the user was created.
     */
    creationDate?: pulumi.Input<string>;
    /**
     * A description associated with the user.
     */
    description?: pulumi.Input<string>;
    /**
     * a convenient map representing an openstackRc file.
     * Note: no password nor sensitive token is set in this map.
     */
    openstackRc?: pulumi.Input<{[key: string]: any}>;
    /**
     * (Sensitive) the password generated for the user. The password can
     * be used with the Openstack API. This attribute is sensitive and will only be
     * retrieve once during creation.
     */
    password?: pulumi.Input<string>;
    /**
     * The id of the public cloud project. If omitted,
     * the `OVH_PROJECT_ID` environment variable is used. DEPRECATED. Use `serviceName` instead.
     */
    projectId?: pulumi.Input<string>;
    /**
     * The name of a role. See `roleNames`.
     */
    roleName?: pulumi.Input<string>;
    /**
     * A list of role names. Values can be: 
     * - administrator,
     * - aiTrainingOperator
     * - authentication
     * - backupOperator
     * - computeOperator
     * - imageOperator
     * - infrastructureSupervisor
     * - networkOperator
     * - networkSecurityOperator
     * - objectstoreOperator
     * - volume_operator
     */
    roleNames?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A list of roles associated with the user.
     */
    roles?: pulumi.Input<pulumi.Input<inputs.CloudUserRole>[]>;
    /**
     * The id of the public cloud project. Conflicts with `projectId`.
     */
    serviceName?: pulumi.Input<string>;
    /**
     * the status of the user. should be normally set to 'ok'.
     */
    status?: pulumi.Input<string>;
    /**
     * the username generated for the user. This username can be used with
     * the Openstack API.
     */
    username?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a CloudUser resource.
 */
export interface CloudUserArgs {
    /**
     * A description associated with the user.
     */
    description?: pulumi.Input<string>;
    /**
     * a convenient map representing an openstackRc file.
     * Note: no password nor sensitive token is set in this map.
     */
    openstackRc?: pulumi.Input<{[key: string]: any}>;
    /**
     * The id of the public cloud project. If omitted,
     * the `OVH_PROJECT_ID` environment variable is used. DEPRECATED. Use `serviceName` instead.
     */
    projectId?: pulumi.Input<string>;
    /**
     * The name of a role. See `roleNames`.
     */
    roleName?: pulumi.Input<string>;
    /**
     * A list of role names. Values can be: 
     * - administrator,
     * - aiTrainingOperator
     * - authentication
     * - backupOperator
     * - computeOperator
     * - imageOperator
     * - infrastructureSupervisor
     * - networkOperator
     * - networkSecurityOperator
     * - objectstoreOperator
     * - volume_operator
     */
    roleNames?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The id of the public cloud project. Conflicts with `projectId`.
     */
    serviceName?: pulumi.Input<string>;
}
