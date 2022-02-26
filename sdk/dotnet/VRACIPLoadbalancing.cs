// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ovh
{
    /// <summary>
    /// Attach a ip loadbalancing to a VRack.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Ovh = Pulumi.Ovh;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var viplb = new Ovh.VRACIPLoadbalancing("viplb", new Ovh.VRACIPLoadbalancingArgs
    ///         {
    ///             IpLoadbalancing = "yyy",
    ///             ServiceName = "xxx",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    [OvhResourceType("ovh:index/vRACIPLoadbalancing:VRACIPLoadbalancing")]
    public partial class VRACIPLoadbalancing : Pulumi.CustomResource
    {
        /// <summary>
        /// The id of the ip loadbalancing.
        /// </summary>
        [Output("ipLoadbalancing")]
        public Output<string> IpLoadbalancing { get; private set; } = null!;

        /// <summary>
        /// The id of the vrack.
        /// </summary>
        [Output("serviceName")]
        public Output<string> ServiceName { get; private set; } = null!;


        /// <summary>
        /// Create a VRACIPLoadbalancing resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public VRACIPLoadbalancing(string name, VRACIPLoadbalancingArgs args, CustomResourceOptions? options = null)
            : base("ovh:index/vRACIPLoadbalancing:VRACIPLoadbalancing", name, args ?? new VRACIPLoadbalancingArgs(), MakeResourceOptions(options, ""))
        {
        }

        private VRACIPLoadbalancing(string name, Input<string> id, VRACIPLoadbalancingState? state = null, CustomResourceOptions? options = null)
            : base("ovh:index/vRACIPLoadbalancing:VRACIPLoadbalancing", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing VRACIPLoadbalancing resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static VRACIPLoadbalancing Get(string name, Input<string> id, VRACIPLoadbalancingState? state = null, CustomResourceOptions? options = null)
        {
            return new VRACIPLoadbalancing(name, id, state, options);
        }
    }

    public sealed class VRACIPLoadbalancingArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The id of the ip loadbalancing.
        /// </summary>
        [Input("ipLoadbalancing", required: true)]
        public Input<string> IpLoadbalancing { get; set; } = null!;

        /// <summary>
        /// The id of the vrack.
        /// </summary>
        [Input("serviceName", required: true)]
        public Input<string> ServiceName { get; set; } = null!;

        public VRACIPLoadbalancingArgs()
        {
        }
    }

    public sealed class VRACIPLoadbalancingState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The id of the ip loadbalancing.
        /// </summary>
        [Input("ipLoadbalancing")]
        public Input<string>? IpLoadbalancing { get; set; }

        /// <summary>
        /// The id of the vrack.
        /// </summary>
        [Input("serviceName")]
        public Input<string>? ServiceName { get; set; }

        public VRACIPLoadbalancingState()
        {
        }
    }
}
