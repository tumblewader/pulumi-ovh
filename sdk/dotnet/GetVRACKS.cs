// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ovh
{
    public static class GetVRACKS
    {
        /// <summary>
        /// Use this data source to get the list of Vrack ids available for your OVH account.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Ovh = Pulumi.Ovh;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var vracks = Output.Create(Ovh.GetVRACKS.InvokeAsync());
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetVRACKSResult> InvokeAsync(InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetVRACKSResult>("ovh:index/getVRACKS:getVRACKS", InvokeArgs.Empty, options.WithDefaults());
    }


    [OutputType]
    public sealed class GetVRACKSResult
    {
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly ImmutableArray<string> Results;

        [OutputConstructor]
        private GetVRACKSResult(
            string id,

            ImmutableArray<string> results)
        {
            Id = id;
            Results = results;
        }
    }
}