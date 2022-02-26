// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ovh

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Use this data source to get the regions of a public cloud project.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-ovh/sdk/go/ovh"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := ovh.GetCloudRegions(ctx, &GetCloudRegionsArgs{
// 			HasServicesUps: []string{
// 				"network",
// 			},
// 			ProjectId: "XXXXXX",
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func GetCloudRegions(ctx *pulumi.Context, args *GetCloudRegionsArgs, opts ...pulumi.InvokeOption) (*GetCloudRegionsResult, error) {
	var rv GetCloudRegionsResult
	err := ctx.Invoke("ovh:index/getCloudRegions:getCloudRegions", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getCloudRegions.
type GetCloudRegionsArgs struct {
	// List of services which has to be UP in regions.
	// Example: "image", "instance", "network", "storage", "volume", "workflow", ...
	// If left blank, returns all regions associated with the project_id.
	HasServicesUps []string `pulumi:"hasServicesUps"`
	// The id of the public cloud project. If omitted,
	// the `OVH_PROJECT_ID` environment variable is used.
	ProjectId string `pulumi:"projectId"`
}

// A collection of values returned by getCloudRegions.
type GetCloudRegionsResult struct {
	HasServicesUps []string `pulumi:"hasServicesUps"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The list of regions associated with the project, filtered by services UP.
	Names     []string `pulumi:"names"`
	ProjectId string   `pulumi:"projectId"`
}

func GetCloudRegionsOutput(ctx *pulumi.Context, args GetCloudRegionsOutputArgs, opts ...pulumi.InvokeOption) GetCloudRegionsResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetCloudRegionsResult, error) {
			args := v.(GetCloudRegionsArgs)
			r, err := GetCloudRegions(ctx, &args, opts...)
			return *r, err
		}).(GetCloudRegionsResultOutput)
}

// A collection of arguments for invoking getCloudRegions.
type GetCloudRegionsOutputArgs struct {
	// List of services which has to be UP in regions.
	// Example: "image", "instance", "network", "storage", "volume", "workflow", ...
	// If left blank, returns all regions associated with the project_id.
	HasServicesUps pulumi.StringArrayInput `pulumi:"hasServicesUps"`
	// The id of the public cloud project. If omitted,
	// the `OVH_PROJECT_ID` environment variable is used.
	ProjectId pulumi.StringInput `pulumi:"projectId"`
}

func (GetCloudRegionsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetCloudRegionsArgs)(nil)).Elem()
}

// A collection of values returned by getCloudRegions.
type GetCloudRegionsResultOutput struct{ *pulumi.OutputState }

func (GetCloudRegionsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetCloudRegionsResult)(nil)).Elem()
}

func (o GetCloudRegionsResultOutput) ToGetCloudRegionsResultOutput() GetCloudRegionsResultOutput {
	return o
}

func (o GetCloudRegionsResultOutput) ToGetCloudRegionsResultOutputWithContext(ctx context.Context) GetCloudRegionsResultOutput {
	return o
}

func (o GetCloudRegionsResultOutput) HasServicesUps() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetCloudRegionsResult) []string { return v.HasServicesUps }).(pulumi.StringArrayOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetCloudRegionsResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetCloudRegionsResult) string { return v.Id }).(pulumi.StringOutput)
}

// The list of regions associated with the project, filtered by services UP.
func (o GetCloudRegionsResultOutput) Names() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetCloudRegionsResult) []string { return v.Names }).(pulumi.StringArrayOutput)
}

func (o GetCloudRegionsResultOutput) ProjectId() pulumi.StringOutput {
	return o.ApplyT(func(v GetCloudRegionsResult) string { return v.ProjectId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetCloudRegionsResultOutput{})
}