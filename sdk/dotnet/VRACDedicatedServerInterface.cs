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
    /// Attach a Dedicated Server Network Interface to a VRack.
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
    ///         var vdsi = new Ovh.VRACDedicatedServerInterface("vdsi", new Ovh.VRACDedicatedServerInterfaceArgs
    ///         {
    ///             InterfaceId = "67890",
    ///             VrackId = "12345",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    [OvhResourceType("ovh:index/vRACDedicatedServerInterface:VRACDedicatedServerInterface")]
    public partial class VRACDedicatedServerInterface : Pulumi.CustomResource
    {
        /// <summary>
        /// The id of dedicated server network interface.
        /// </summary>
        [Output("interfaceId")]
        public Output<string> InterfaceId { get; private set; } = null!;

        /// <summary>
        /// The id of the vrack.
        /// </summary>
        [Output("vrackId")]
        public Output<string> VrackId { get; private set; } = null!;


        /// <summary>
        /// Create a VRACDedicatedServerInterface resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public VRACDedicatedServerInterface(string name, VRACDedicatedServerInterfaceArgs args, CustomResourceOptions? options = null)
            : base("ovh:index/vRACDedicatedServerInterface:VRACDedicatedServerInterface", name, args ?? new VRACDedicatedServerInterfaceArgs(), MakeResourceOptions(options, ""))
        {
        }

        private VRACDedicatedServerInterface(string name, Input<string> id, VRACDedicatedServerInterfaceState? state = null, CustomResourceOptions? options = null)
            : base("ovh:index/vRACDedicatedServerInterface:VRACDedicatedServerInterface", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing VRACDedicatedServerInterface resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static VRACDedicatedServerInterface Get(string name, Input<string> id, VRACDedicatedServerInterfaceState? state = null, CustomResourceOptions? options = null)
        {
            return new VRACDedicatedServerInterface(name, id, state, options);
        }
    }

    public sealed class VRACDedicatedServerInterfaceArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The id of dedicated server network interface.
        /// </summary>
        [Input("interfaceId", required: true)]
        public Input<string> InterfaceId { get; set; } = null!;

        /// <summary>
        /// The id of the vrack.
        /// </summary>
        [Input("vrackId", required: true)]
        public Input<string> VrackId { get; set; } = null!;

        public VRACDedicatedServerInterfaceArgs()
        {
        }
    }

    public sealed class VRACDedicatedServerInterfaceState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The id of dedicated server network interface.
        /// </summary>
        [Input("interfaceId")]
        public Input<string>? InterfaceId { get; set; }

        /// <summary>
        /// The id of the vrack.
        /// </summary>
        [Input("vrackId")]
        public Input<string>? VrackId { get; set; }

        public VRACDedicatedServerInterfaceState()
        {
        }
    }
}
