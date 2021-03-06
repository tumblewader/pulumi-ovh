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
    /// Manage a vrack network for your IP Loadbalancing service.
    /// </summary>
    [OvhResourceType("ovh:index/iPLoadbalancingVRACNetwork:IPLoadbalancingVRACNetwork")]
    public partial class IPLoadbalancingVRACNetwork : Pulumi.CustomResource
    {
        /// <summary>
        /// Human readable name for your vrack network
        /// </summary>
        [Output("displayName")]
        public Output<string?> DisplayName { get; private set; } = null!;

        /// <summary>
        /// This attribute is there for documentation purpose only and isnt passed to the OVH API as it may conflicts with http/tcp farms `vrack_network_id` attribute
        /// </summary>
        [Output("farmIds")]
        public Output<ImmutableArray<int>> FarmIds { get; private set; } = null!;

        /// <summary>
        /// An IP block used as a pool of IPs by this Load Balancer to connect to the servers in this private network. The blck must be in the private network and reserved for the Load Balancer
        /// </summary>
        [Output("natIp")]
        public Output<string> NatIp { get; private set; } = null!;

        /// <summary>
        /// The internal name of your IP load balancing
        /// </summary>
        [Output("serviceName")]
        public Output<string> ServiceName { get; private set; } = null!;

        /// <summary>
        /// IP block of the private network in the vRack
        /// </summary>
        [Output("subnet")]
        public Output<string> Subnet { get; private set; } = null!;

        /// <summary>
        /// VLAN of the private network in the vRack. 0 if the private network is not in a VLAN
        /// </summary>
        [Output("vlan")]
        public Output<int> Vlan { get; private set; } = null!;

        /// <summary>
        /// (Required) Internal Load Balancer identifier of the vRack private network
        /// </summary>
        [Output("vrackNetworkId")]
        public Output<int> VrackNetworkId { get; private set; } = null!;


        /// <summary>
        /// Create a IPLoadbalancingVRACNetwork resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public IPLoadbalancingVRACNetwork(string name, IPLoadbalancingVRACNetworkArgs args, CustomResourceOptions? options = null)
            : base("ovh:index/iPLoadbalancingVRACNetwork:IPLoadbalancingVRACNetwork", name, args ?? new IPLoadbalancingVRACNetworkArgs(), MakeResourceOptions(options, ""))
        {
        }

        private IPLoadbalancingVRACNetwork(string name, Input<string> id, IPLoadbalancingVRACNetworkState? state = null, CustomResourceOptions? options = null)
            : base("ovh:index/iPLoadbalancingVRACNetwork:IPLoadbalancingVRACNetwork", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing IPLoadbalancingVRACNetwork resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static IPLoadbalancingVRACNetwork Get(string name, Input<string> id, IPLoadbalancingVRACNetworkState? state = null, CustomResourceOptions? options = null)
        {
            return new IPLoadbalancingVRACNetwork(name, id, state, options);
        }
    }

    public sealed class IPLoadbalancingVRACNetworkArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Human readable name for your vrack network
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        [Input("farmIds")]
        private InputList<int>? _farmIds;

        /// <summary>
        /// This attribute is there for documentation purpose only and isnt passed to the OVH API as it may conflicts with http/tcp farms `vrack_network_id` attribute
        /// </summary>
        public InputList<int> FarmIds
        {
            get => _farmIds ?? (_farmIds = new InputList<int>());
            set => _farmIds = value;
        }

        /// <summary>
        /// An IP block used as a pool of IPs by this Load Balancer to connect to the servers in this private network. The blck must be in the private network and reserved for the Load Balancer
        /// </summary>
        [Input("natIp", required: true)]
        public Input<string> NatIp { get; set; } = null!;

        /// <summary>
        /// The internal name of your IP load balancing
        /// </summary>
        [Input("serviceName", required: true)]
        public Input<string> ServiceName { get; set; } = null!;

        /// <summary>
        /// IP block of the private network in the vRack
        /// </summary>
        [Input("subnet", required: true)]
        public Input<string> Subnet { get; set; } = null!;

        /// <summary>
        /// VLAN of the private network in the vRack. 0 if the private network is not in a VLAN
        /// </summary>
        [Input("vlan")]
        public Input<int>? Vlan { get; set; }

        public IPLoadbalancingVRACNetworkArgs()
        {
        }
    }

    public sealed class IPLoadbalancingVRACNetworkState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Human readable name for your vrack network
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        [Input("farmIds")]
        private InputList<int>? _farmIds;

        /// <summary>
        /// This attribute is there for documentation purpose only and isnt passed to the OVH API as it may conflicts with http/tcp farms `vrack_network_id` attribute
        /// </summary>
        public InputList<int> FarmIds
        {
            get => _farmIds ?? (_farmIds = new InputList<int>());
            set => _farmIds = value;
        }

        /// <summary>
        /// An IP block used as a pool of IPs by this Load Balancer to connect to the servers in this private network. The blck must be in the private network and reserved for the Load Balancer
        /// </summary>
        [Input("natIp")]
        public Input<string>? NatIp { get; set; }

        /// <summary>
        /// The internal name of your IP load balancing
        /// </summary>
        [Input("serviceName")]
        public Input<string>? ServiceName { get; set; }

        /// <summary>
        /// IP block of the private network in the vRack
        /// </summary>
        [Input("subnet")]
        public Input<string>? Subnet { get; set; }

        /// <summary>
        /// VLAN of the private network in the vRack. 0 if the private network is not in a VLAN
        /// </summary>
        [Input("vlan")]
        public Input<int>? Vlan { get; set; }

        /// <summary>
        /// (Required) Internal Load Balancer identifier of the vRack private network
        /// </summary>
        [Input("vrackNetworkId")]
        public Input<int>? VrackNetworkId { get; set; }

        public IPLoadbalancingVRACNetworkState()
        {
        }
    }
}
