// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ovh
{
    public static class GetMeSSHKeys
    {
        /// <summary>
        /// Use this data source to retrieve list of names of the account's SSH keys.
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
        ///         var mykeys = Output.Create(Ovh.GetMeSSHKeys.InvokeAsync());
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetMeSSHKeysResult> InvokeAsync(InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetMeSSHKeysResult>("ovh:index/getMeSSHKeys:getMeSSHKeys", InvokeArgs.Empty, options.WithDefaults());
    }


    [OutputType]
    public sealed class GetMeSSHKeysResult
    {
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The list of the names of all the SSH keys.
        /// </summary>
        public readonly ImmutableArray<string> Names;

        [OutputConstructor]
        private GetMeSSHKeysResult(
            string id,

            ImmutableArray<string> names)
        {
            Id = id;
            Names = names;
        }
    }
}